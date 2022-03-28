from paka.cmark import lowlevel

from .types import EventType
from .node import Node


class NodeIter:

    def __init__(self, root: Node) -> None:
        self._root = root
        self._iter = lowlevel.iter_new(root._node)

    def __iter__(self):
        return self

    def __next__(self):
        if self.next() != EventType.EVENT_DONE:
            return self.get_node()
        raise StopIteration

    def free(self):
        lowlevel.iter_free(self._iter)

    def next(self) -> EventType:
        """Advance to next node and return event type.

        :returns: One of EventType.
        """
        return EventType(lowlevel.iter_next(self._iter))

    def get_node(self) -> Node:
        """Return current node."""
        return Node(lowlevel.iter_get_node(self._iter))

    def get_event_type(self) -> EventType:
        """Return current event type.

        :returns: One of EventType.
        """
        return EventType(lowlevel.iter_get_event_type(self._iter)) 

    def get_root(self) -> Node:
        """Return root node."""
        return Node(lowlevel.iter_get_root(self._iter))

    def iter_reset(self, node: Node, event: EventType):
        """Reset the iterator.

        :param node: Node to make current.
        :param event: EventType to make current.
            
        :return: None
        """
        return lowlevel.iter_reset(self._iter, node._node, event.value)
