from typing import Optional

from paka.cmark import lowlevel

from .types import Delimiter, ListType, NodeType


class Node:
    def __init__(self, node) -> None:
        self._node = node

    def free(self):
        """Free memory for node and its children (if any)."""
        lowlevel.node_free(self._node)

    def __visit(self, func: str):
        n = getattr(lowlevel, func)(self._node)
        if n:
            return self.__class__(n)
        return None

    def next(self) -> Optional["Node"]:
        """Return next node, if available.

        :returns: A node or None.

        """
        return self.__visit("node_next")

    def previous(self) -> Optional["Node"]:
        """Return previous node, if available.

        :returns: A node or None.

        """
        return self.__visit("node_previous")

    def parent(self) -> Optional["Node"]:
        """Return a parent of node, if available.

        :returns: A node or None.

        """
        return self.__visit("node_parent")

    def first_child(self) -> Optional["Node"]:
        """Return first child of node, if available.

        :returns: A node or None.

        """
        return self.__visit("node_first_child")

    def last_child(self) -> Optional["Node"]:
        """Return last child of node, if available.

        :returns: A node or None.

        """
        return self.__visit("node_last_child")

    def __operate(self, func: str, n: "Node"):
        res = getattr(lowlevel, func)(self._node, n._node)
        return bool(res)

    def insert_before(self, sibling: "Node") -> bool:
        """Insert sibling before node.

        :return: ``True`` on success, ``False`` on failure.
        """
        return self.__operate("node_insert_before", sibling)

    def insert_after(self, sibling: "Node") -> bool:
        """Insert sibling after node.

        :return: ``True`` on success, ``False`` on failure.
        """
        return self.__operate("node_insert_after", sibling)

    def prepend_child(self, child: "Node") -> bool:
        """Prepend child to children of node.

        :return: ``True`` on success, ``False`` on failure.
        """
        return self.__operate("node_prepend_child", child)

    def append_child(self, child: "Node") -> bool:
        """Append child to children of node.

        :returns: ``True`` on success, ``False`` on failure.
        """
        return self.__operate("node_append_child", child)

    def get_type(self) -> NodeType:
        """Return type of node.

        :returns: One of NodeType.
        """
        return NodeType(lowlevel.node_get_type(self._node))

    def __get_info(self, func: str, free: bool = False) -> str:
        ct = getattr(lowlevel, func)(self._node)
        return lowlevel.text_from_c(ct, free)

    def __set_info(self, func: str, info: str) -> bool:
        ci = lowlevel.text_to_c(info)
        ct: int = getattr(lowlevel, func)(self._node, ci)
        return bool(ct)

    def get_type_string(self) -> str:
        """Return type of node as string."""
        return self.__get_info("node_get_type_string")

    def get_fence_info(self) -> Optional[str]:
        """Return fence info from fenced code block.

        For nodes having type other than :py:data:`NODE_CODE_BLOCK`
        returns None.

        """
        return self.__get_info("node_get_fence_info")

    def set_fence_info(self, info: str) -> bool:
        """Set fence info of fenced code block.

        :param info: Fence info.

        :return: ``True`` on success, ``False`` on failure.
        """
        return self.__set_info("node_set_fence_info", info)

    def get_literal(self) -> Optional[str]:
        """Return string contents of node.

        Returns None for nodes having type other than
        :py:data:`NODE_HTML_BLOCK`, :py:data:`NODE_TEXT`,
        :py:data:`NODE_HTML_INLINE`, :py:data:`NODE_CODE`
        or :py:data:`NODE_CODE_BLOCK`.

        """
        return self.__get_info("node_get_literal")

    def set_literal(self, contents: str) -> bool:
        """Set string contents of node.

        :param contents: New contents of node.

        :return: ``True`` on success, ``False`` on failure.
        """
        return self.__set_info("node_set_literal", contents)

    def get_heading_level(self) -> int:
        """Return level of heading.

        :return: ``[1, 6]`` for headings, ``0`` for non-heading nodes.
        """
        return lowlevel.node_get_heading_level(self._node)

    def set_heading_level(self, level: int):
        """Set level of heading.

        :param level: ``[1, 6]``

        :return: ``True`` on success, ``False`` on failure.
        """
        res = lowlevel.node_set_heading_level(self._node, level)
        return bool(res)

    def get_list_type(self) -> ListType:
        """Return list type of node.

        :returns: One of ListType.
        """
        return ListType(lowlevel.node_get_list_type(self._node))

    def set_list_type(self, list_type: ListType) -> bool:
        """Set the list type of node.

        :param list_type: One of ListType.

        :return: ``True`` on success, ``False`` on failure.
        """
        res = lowlevel.node_set_list_type(self._node, list_type.value)
        return bool(res)

    def get_list_delim(self) -> Delimiter:
        """Return type of list delimiter.

        :returns: One of Delimiter.
        """
        return Delimiter(lowlevel.node_get_list_delim(self._node))

    def set_list_delim(self, list_delim: Delimiter):
        """Set the type of list delimiter for node.

        :param list_delim: One of Delimiter.

        :return: ``True`` on success, ``False`` on failure.
        """
        res = lowlevel.node_set_list_delim(self._node, list_delim)
        return bool(res)

    def get_list_start(self) -> int:
        """Return starting number of list.
        :return: Starting number of an ordered list or ``0``.
        """
        return lowlevel.node_get_list_start(self._node)

    def set_list_start(self, start: int) -> bool:
        """Set starting number of ordered list.

        :param start: Starting number.

        :return: ``True`` on success, ``False`` on failure.
        """
        res = lowlevel.node_set_list_start(self._node, start)
        return bool(res)

    def get_list_tight(self) -> int:
        """Return 1 if node is a tight list.

        :return: ``1`` if node is a tight list, ``0`` otherwise.
        """
        return lowlevel.node_get_list_tight(self._node)

    def set_list_tight(self, tight: int):
        """Set tightness of list.

        :param tight: ``1`` for tight, ``0`` for loose.

        :return: ``1`` on success, ``0`` on failure.
        """
        res = lowlevel.node_set_list_tight(self._node, tight)
        return int(res)

    def get_url(self) -> Optional[str]:
        """Return URL of image or link, or None."""
        return self.__get_info("node_get_url")

    def set_url(self, url: str) -> bool:
        """Set URL of image or link.

        :param url: New URL.

        :return: ``True`` on success, ``False`` on failure.
        """
        return self.__set_info("node_set_url", url)

    def get_title(self) -> Optional[str]:
        """Return title of image or link, or None."""
        return self.__get_info("node_get_title")

    def set_title(self, title: str) -> bool:
        """Set title of image or link.

        :param title: New title.

        :return: ``True`` on success, ``False`` on failure.
        """
        return self.__set_info("node_set_title", title)

    def get_start_line(self) -> int:
        """Return line on which node begins.
        :return: Line number (starts from ``1``).
        """
        return lowlevel.node_get_start_line(self._node)

    def get_start_column(self) -> int:
        """Return column at which node begins.

        :return: Column number (starts from ``1``).
        """
        return lowlevel.node_get_start_column(self._node)

    def get_end_line(self) -> int:
        """Return line on which node ends.

        :return: Line number (starts from ``1``).
        """
        return lowlevel.node_get_end_line(self._node)

    def get_end_column(self) -> int:
        """Return column at which node ends.

        :return: Column number (starts from ``1``).
        """
        return lowlevel.node_get_end_column(self._node)
