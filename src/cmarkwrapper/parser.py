from paka import cmark
from paka.cmark import lowlevel

from .types import Option
from .node import Node



class MarkdownParser:

    version = cmark.get_version()

    def __init__(self, md: str, encoding: str = "utf-8") -> None:
        self._md = md
        self._encoding = encoding  # TODO support other encoding

    def parse_document(self, options: Option=Option.OPT_DEFAULT):
        """parse markdown to a node tree."""
        cmd = lowlevel.text_to_c(self._md)
        root = lowlevel.parse_document(cmd, len(cmd), options.value)
        return Node(root)
