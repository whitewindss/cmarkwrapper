from typing import Union

from paka import cmark

from .types import Option, LineBreaks


def markdown_to_html(
    text: str,
    breaks: Union[bool, LineBreaks] = False,
    safe: bool = True,
    sourcepos: bool = False,
    smart: Option = Option.OPT_SMART,
) -> str:
    r"""Convert markup to HTML.

    :param text: Text marked up with `CommonMark <http://commonmark.org>`_.
    :param breaks: bool or LineBreaks
        How line breaks in text will be rendered. If ``True``,
        ``"soft"``, or :py:attr:`LineBreaks.soft` -- as newlines
        (``\n``). If ``False`` -- as spaces. If ``"hard"`` or
        :py:attr:`LineBreaks.hard` -- as ``<br />``\ s.
    :param safe: When ``True``, replace raw HTML (that was present in ``text``)with HTML comment.
    :param sourcepos: If ``True``, add ``data-sourcepos`` attribute to block elements(that is, use ``CMARK_OPT_SOURCEPOS``).
    :param smart: Use :py:data:`~cmarkwrapper.types.OPTION.OPT_SMART`.

    :return: HTML string.
    """
    if isinstance(breaks, LineBreaks):
        breaks = breaks.value 
    return cmark.to_html(text, breaks, safe, sourcepos, smart.value)


def markdown_to_xml(text: str, sourcepos: bool = False, smart: Option = Option.OPT_SMART) -> str:
    r"""Convert markup to XML.
    
    :param text: Text marked up with `CommonMark <http://commonmark.org>`_.
    :param sourcepos: If ``True``, add ``sourcepos`` attribute to all block elements(that is, use ``CMARK_OPT_SOURCEPOS``).
    :param smart: Use :py:data:`~cmarkwrapper.types.OPTION.OPT_SMART`.

    :return: XML string.
    """
    return cmark.to_xml(text, sourcepos, smart.value)


def markdown_to_commonmark(
    text: str, breaks: Union[bool, LineBreaks] = False, width: int = 0, smart: Option = Option.OPT_SMART
) -> str:
    r"""Convert markup to CommonMark.
    
    :param text: Text marked up with `CommonMark <http://commonmark.org>`_.
    :param breaks: bool or LineBreaks
        How line breaks will be rendered. If ``True``,
        ``"soft"``, or :py:attr:`LineBreaks.soft` -- as newlines
        (``\n``). If ``False`` -- as spaces. If ``"hard"`` or
        :py:attr:`LineBreaks.hard` -- “soft break nodes” (single
        newlines) are rendered as two spaces and ``\n``.
    :param width: Wrap width of output by inserting line breaks (default is``0``—no wrapping). Has no effect if ``breaks`` are set to be``"hard"`` (e.g. with :py:attr:`LineBreaks.hard`).
    :param smart: Use :py:data:`~cmarkwrapper.types.OPTION.OPT_SMART`.

    :return: CommonMark string.

    """
    if isinstance(breaks, LineBreaks):
        breaks = breaks.value
    return cmark.to_commonmark(text, breaks, width, smart.value)


def markdown_to_man(
    text: str, breaks: Union[bool, LineBreaks] = False, width: int = 0, smart: Option = Option.OPT_SMART
) -> str:
    r"""Convert markup to groff man page.
    
    :param text: Text marked up with `CommonMark <http://commonmark.org>`_.
    :param breaks: bool or LineBreaks
        How line breaks will be rendered. If ``True``,
        ``"soft"``, or :py:attr:`LineBreaks.soft` -- “soft break nodes”
        (single newlines) are rendered as newlines (``\n``). If ``False``
        -- “soft break nodes” are rendered as spaces. If ``"hard"`` or
        :py:attr:`LineBreaks.hard` -- “soft break nodes” are rendered
        as ``.PD 0\n.P\n.PD\n``.
    :param width: Wrap width of output by inserting line breaks (default is``0``—no wrapping). Has no effect if ``breaks`` are ``False``.
    :param smart: Use :py:data:`~paka.cmark.lowlevel.OPT_SMART`.

    :return: Page without the header.

    """
    if isinstance(breaks, LineBreaks):
        breaks = breaks.value
    return cmark.to_man(text, breaks, width, smart.value)


def markdown_to_latex(
    text: str, breaks: Union[bool, LineBreaks] = False, width: int = 0, smart: Option = Option.OPT_SMART
) -> str:
    r"""Convert markup to LaTeX.
    
    :param text: Text marked up with `CommonMark <http://commonmark.org>`_.
    :param breaks: bool or LineBreaks
        How line breaks will be rendered. If ``True``,
        ``"soft"``, or :py:attr:`LineBreaks.soft` -- as newlines.
        If ``False`` -- “soft break nodes” (single newlines) are
        rendered as spaces. If ``"hard"`` or :py:attr:`LineBreaks.hard`
        -- “soft break nodes” are rendered as ``\\\n``.
    :param width: Wrap width of output by inserting line breaks (default is
        ``0``—no wrapping). Has no effect if ``breaks`` are ``False``.
    :param smart: Use :py:data:`~cmarkwrapper.types.OPTION.OPT_SMART`.

    :return: LaTeX document.
    """
    if isinstance(breaks, LineBreaks):
        breaks = breaks.value
    return cmark.to_latex(text, breaks, width, smart.value)
