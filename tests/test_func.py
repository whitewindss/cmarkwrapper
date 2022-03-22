from cmarkwrapper import markdown_to_html


def test_convert_html():
    html = markdown_to_html(
"""
*Italic*    _Italic_  
**Bold**	__Bold__  

![image](https://commonmark.org/help/images/favicon.png)
"""
    )
    assert len(html) > 1


def test_convert_html_italic():
    assert markdown_to_html(
"""
*Italic*    _Italic_
"""
    ) ==  "<p><em>Italic</em>    <em>Italic</em></p>\n"


def test_convert_html_bold():
    assert markdown_to_html(
"""
**Bold**    __Bold__
"""
    ) == "<p><strong>Bold</strong>    <strong>Bold</strong></p>\n"