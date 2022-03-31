from paka.cmark import lowlevel

from .node import Node
from .types import IterEvent


class NodeIter:
    def __init__(self, root: Node) -> None:
        self._root = root
        self._iter = lowlevel.iter_new(root._node)

    def __iter__(self):
        return self

    def __next__(self):
        if self.next() != IterEvent.EVENT_DONE:
            return self.get_node()
        raise StopIteration

    def free(self):
        lowlevel.iter_free(self._iter)

    def next(self) -> IterEvent:
        """Advance to next node and return event type.

        :returns: One of IterEvent.
        """
        return IterEvent(lowlevel.iter_next(self._iter))

    def get_node(self) -> Node:
        """Return current node."""
        return Node(lowlevel.iter_get_node(self._iter))

    def get_event_type(self) -> IterEvent:
        """Return current event type.

        :returns: One of IterEvent.
        """
        return IterEvent(lowlevel.iter_get_event_type(self._iter))

    def get_root(self) -> Node:
        """Return root node."""
        return Node(lowlevel.iter_get_root(self._iter))

    def iter_reset(self, node: Node, event: IterEvent):
        """Reset the iterator.

        :param node: Node to make current.
        :param event: IterEvent to make current.

        :return: None
        """
        return lowlevel.iter_reset(self._iter, node._node, event.value)
