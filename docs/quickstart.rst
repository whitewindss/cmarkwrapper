Quickstart
==========

``cmarkwrapper`` 是一个基于 `paka.cmark <https://github.com/kapyshin/paka.cmark/>`_ 的 `cmark <https://github.com/commonmark/cmark/>`_ 封装，更加符合使用习惯。


安装
---------
使用 ``pypi``  

``pip install cmarkwrapper``

或使用 ``git+``  

``pip install git+https://github.com/yangfan9702/cmarkwrapper.git``


基本使用
---------
.. code-block:: python

    from cmarkwrapper import markdown_to_html

    html = markdown_to_html(
    """
    *Italic*    _Italic_  
    **Bold**    __Bold__  

    ![image](https://commonmark.org/help/images/favicon.png)
    """
    )
    print(html)


进阶使用
---------
.. code-block:: python

    from cmarkwrapper import MarkdownParser, NodeIter

    parser = MarkdownParser(
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
    )

    node = parser.parse_document()  # root

    iter = NodeIter(node)
    for node in iter:
        print(f"{iter.get_event_type()} {(node.get_type_string() or ''):10} {(node.get_literal() or ''):10} {node.get_url()}")

    iter.free()
    node.free()


