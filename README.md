# cmarkwrapper
![Python Version](https://img.shields.io/badge/python-v3.7.5-brightgreen)
![System Platform](https://img.shields.io/badge/platform-ubuntu-brightgreen.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Documentation Status](https://readthedocs.org/projects/cmarkwrapper/badge/?version=latest)](https://cmarkwrapper.readthedocs.io/zh/latest/?badge=latest)

`cmarkwrapper`是一个基于[paka.cmark](https://github.com/kapyshin/paka.cmark)的[cmark](https://github.com/commonmark/cmark) 封装，更加符合使用习惯。

## 安装
**使用 `pypi`**  
`pip install cmarkwrapper`

**或使用 `git+`**  
`pip install git+https://github.com/yangfan9702/cmarkwrapper.git`


## 使用
```python
from cmarkwrapper import markdown_to_html

html = markdown_to_html(
"""
*Italic*    _Italic_  
**Bold**    __Bold__  

![image](https://commonmark.org/help/images/favicon.png)
"""
)
print(html)
```

# 文档
Documentation is on [Read the Docs](https://cmarkwrapper.readthedocs.io/en/latest/). Code repository and issue tracker are on [GitHub](https://github.com/yangfan9702/cmarkwrapper).