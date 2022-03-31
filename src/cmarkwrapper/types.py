from enum import Enum

from paka.cmark import lowlevel


class Option(int, Enum):

    OPT_DEFAULT = lowlevel.OPT_DEFAULT  # type: int
    """Default options."""

    OPT_HARDBREAKS = lowlevel.OPT_HARDBREAKS  # type: int
    """Render “soft break” nodes as hard line breaks."""

    OPT_NOBREAKS = lowlevel.OPT_NOBREAKS  # type: int
    """Render “soft break” nodes as spaces."""

    OPT_SOURCEPOS = lowlevel.OPT_SOURCEPOS  # type: int
    """Render with “sourcepos” information."""

    OPT_UNSAFE = lowlevel.OPT_UNSAFE  # type: int
    """渲染时允许原始的HTML和不安全的链接"""

    OPT_SMART = lowlevel.OPT_SMART  # type: int
    """Render straight quotes as curly, ``---`` as em dash, ``--`` as en dash."""


class IterEvent(int, Enum):
    """迭代事件类型"""

    EVENT_ENTER = lowlevel.EVENT_ENTER  # type: int
    """进入节点"""

    EVENT_EXIT = lowlevel.EVENT_EXIT  # type: int
    """退出节点"""

    EVENT_DONE = lowlevel.EVENT_DONE  # type: int
    """迭代完成"""


class NodeType(int, Enum):
    "节点类型"

    NODE_NONE = lowlevel.NODE_NONE  # type: int
    """Error status."""

    NODE_CODE_BLOCK = lowlevel.NODE_CODE_BLOCK  # type: int
    """代码块"""

    NODE_HTML_BLOCK = lowlevel.NODE_HTML_BLOCK  # type: int
    """原始HTML块"""

    NODE_DOCUMENT = lowlevel.NODE_DOCUMENT  # type: int
    """文档"""

    NODE_BLOCK_QUOTE = lowlevel.NODE_BLOCK_QUOTE  # type: int
    """引用块"""

    NODE_LIST = lowlevel.NODE_LIST  # type: int
    """列表"""

    NODE_ITEM = lowlevel.NODE_ITEM  # type: int
    """List item."""

    NODE_CUSTOM_BLOCK = lowlevel.NODE_CUSTOM_BLOCK  # type: int
    """Block of custom."""

    NODE_PARAGRAPH = lowlevel.NODE_PARAGRAPH  # type: int
    """段落"""

    NODE_HEADING = lowlevel.NODE_HEADING  # type: int
    """标题"""

    NODE_THEMATIC_BREAK = lowlevel.NODE_THEMATIC_BREAK  # type: int
    """Thematic break."""

    NODE_FIRST_BLOCK = lowlevel.NODE_FIRST_BLOCK  # type: int
    """起始块"""

    NODE_LAST_BLOCK = lowlevel.NODE_LAST_BLOCK  # type: int
    """结束块"""

    NODE_TEXT = lowlevel.NODE_TEXT  # type: int
    """文本"""

    NODE_SOFTBREAK = lowlevel.NODE_SOFTBREAK  # type: int
    """Soft break."""

    NODE_LINEBREAK = lowlevel.NODE_LINEBREAK  # type: int
    """Line break."""

    NODE_CODE = lowlevel.NODE_CODE  # type: int
    """行内代码"""

    NODE_HTML_INLINE = lowlevel.NODE_HTML_INLINE  # type: int
    """行内HTML"""

    NODE_CUSTOM_INLINE = lowlevel.NODE_CUSTOM_INLINE  # type: int
    """Inline custom."""

    NODE_EMPH = lowlevel.NODE_EMPH  # type: int
    """强调"""

    NODE_STRONG = lowlevel.NODE_STRONG  # type: int
    """Strong emphasis."""

    NODE_LINK = lowlevel.NODE_LINK  # type: int
    """链接"""

    NODE_IMAGE = lowlevel.NODE_IMAGE  # type: int
    """图片"""

    NODE_FIRST_INLINE = lowlevel.NODE_FIRST_INLINE  # type: int
    """First inline."""

    NODE_LAST_INLINE = lowlevel.NODE_LAST_INLINE  # type: int
    """Last inline."""


class ListType(int, Enum):

    BULLET_LIST = lowlevel.BULLET_LIST  # type: int
    """无序号列表"""

    ORDERED_LIST = lowlevel.ORDERED_LIST  # type: int
    """带序号列表"""

    NO_LIST = lowlevel.NO_LIST  # type: int
    """非列表"""


class Delimiter(int, Enum):
    """分隔符"""

    PAREN_DELIM = lowlevel.PAREN_DELIM  # type: int
    """``)``"""

    PERIOD_DELIM = lowlevel.PERIOD_DELIM  # type: int
    """``.``"""

    NO_DELIM = lowlevel.NO_DELIM  # type: int
    """非分隔符"""


class LineBreaks(str, Enum):
    """换行符将被渲染成？"""

    soft = "soft"
    r"""As ``\n``\ s."""

    hard = "hard"
    r"""As ``<br />``\ s."""
