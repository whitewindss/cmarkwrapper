from paka import cmark
from paka.cmark import lowlevel

from .node import Node


class MarkdownConverter:

    version = cmark.get_version()

    def __init__(self, md: str, encoding: str = "utf-8") -> None:
        self._md = md
        self._encoding = encoding  # TODO support other encoding

    def to_html(self, breaks=False, safe=True, sourcepos=False, smart=False) -> str:
        """Convert markup to HTML."""
        return cmark.to_html(self._md, breaks, safe, sourcepos, smart)

    def to_xml(self, sourcepos=False, smart=False) -> str:
        """Convert markup to XML."""
        return cmark.to_xml(self._md, sourcepos, smart)

    def to_commonmark(self, breaks=False, width=0, smart=False) -> str:
        """Convert markup to CommonMark."""
        return cmark.to_commonmark(self._md, breaks, width, smart)

    def to_man(self, breaks=False, width=0, smart=False) -> str:
        """Convert markup to groff man page."""
        return cmark.to_man(self._md, breaks, width, smart)

    def to_latex(self, breaks=False, width=0, smart=False) -> str:
        """Convert markup to LaTeX."""
        return cmark.to_latex(self._md, breaks, width, smart)

    def parse_document(self, options: int = 0):
        cmd = lowlevel.text_to_c(self._md)
        root = lowlevel.parse_document(cmd, len(cmd), options)
        return Node(root)
