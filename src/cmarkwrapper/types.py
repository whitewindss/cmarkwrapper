from paka.cmark import lowlevel


class NodeType:
    NODE_NONE = lowlevel.NODE_NONE
    """Error status."""
    NODE_HTML_BLOCK = lowlevel.NODE_HTML_BLOCK
    """Raw HTML block."""
    NODE_DOCUMENT = lowlevel.NODE_DOCUMENT
    """Document."""
    NODE_BLOCK_QUOTE = lowlevel.NODE_BLOCK_QUOTE
    """Block quote."""
    NODE_LIST = lowlevel.NODE_LIST
    """List."""
    NODE_ITEM = lowlevel.NODE_ITEM
    """List item."""
    NODE_CUSTOM_BLOCK = lowlevel.NODE_CUSTOM_BLOCK
    """Block of custom."""
    NODE_PARAGRAPH = lowlevel.NODE_PARAGRAPH
    """Paragraph."""
    NODE_HEADING = lowlevel.NODE_HEADING
    """Heading."""
    NODE_THEMATIC_BREAK = lowlevel.NODE_THEMATIC_BREAK
    """Thematic break."""
    NODE_FIRST_BLOCK = lowlevel.NODE_FIRST_BLOCK
    """First block."""
    NODE_LAST_BLOCK = lowlevel.NODE_LAST_BLOCK
    """Last block."""
    NODE_TEXT = lowlevel.NODE_TEXT
    """Text."""
    NODE_SOFTBREAK = lowlevel.NODE_SOFTBREAK
    """Soft break."""
    NODE_LINEBREAK = lowlevel.NODE_LINEBREAK
    """Line break."""
    NODE_CODE = lowlevel.NODE_CODE
    """Inline code."""
    NODE_HTML_INLINE = lowlevel.NODE_HTML_INLINE
    """Inline HTML."""
    NODE_CUSTOM_INLINE = lowlevel.NODE_CUSTOM_INLINE
    """Inline custom."""
    NODE_EMPH = lowlevel.NODE_EMPH
    """Emphasis."""
    NODE_STRONG = lowlevel.NODE_STRONG
    """Strong emphasis."""
    NODE_LINK = lowlevel.NODE_LINK
    """Link."""
    NODE_IMAGE = lowlevel.NODE_IMAGE
    """Image."""
    NODE_FIRST_INLINE = lowlevel.NODE_FIRST_INLINE
    """First inline."""
    NODE_LAST_INLINE = lowlevel.NODE_LAST_INLINE
    """Last inline."""
