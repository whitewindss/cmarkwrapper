from cmarkwrapper import MarkdownParser, NodeIter

root = MarkdownParser(
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
iter = NodeIter(root)


def teardown():
    iter.free()
    root.free()


def test_iter_node():
    for node in iter:
        print(
            f"{node.get_start_line():3} {node.get_type_string():10} {node.get_literal()}"
        )
