from cmarkwrapper import MarkdownConverter



def test_get_version():
    assert MarkdownConverter.version == "0.30.2"

def test_convert_html():
    converter = MarkdownConverter(
"""
*Italic*    _Italic_  
**Bold**	__Bold__  


![image](https://commonmark.org/help/images/favicon.png)
"""
    )
    html = converter.to_html()
    assert len(html) > 1

def test_convert_html_italic():
    assert MarkdownConverter(
"""
*Italic*    _Italic_
"""
    ).to_html() == "<p><em>Italic</em>    <em>Italic</em></p>\n"

def test_convert_html_bold():
    assert MarkdownConverter(
"""
**Bold**    __Bold__
"""
    ).to_html() == "<p><strong>Bold</strong>    <strong>Bold</strong></p>\n"