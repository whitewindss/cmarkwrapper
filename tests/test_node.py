from cmarkwrapper import MarkdownConverter

root = MarkdownConverter(
"""
*Italic*  

**Bold**  

# Heading 1

## Heading 2

[Link](https://commonmark.org/help/)  

![Image](https://commonmark.org/help/images/favicon.png)  

> Blockquote

* List
* List
* List

"""
).parse_document()


def teardown():
    root.free()

def test_get_start_line():
    assert root.get_start_line() == 1

def test_get_type_string():
    assert root.get_type_string() == "document"

def test_next():
    c = root.first_child()
    assert c
    d = c.next()
    assert d
    assert d.get_type_string() == "paragraph"

def test_previous():
    c = root.last_child()
    assert c
    d = c.previous()
    assert d
    assert d.get_type_string() == "block_quote"

def test_first_child():
    c = root.first_child()
    assert c
    assert c.get_type_string() == "paragraph"

def test_last_child():
    c = root.last_child()
    assert c
    assert c.get_type_string() == "list"