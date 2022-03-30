from cmarkwrapper import MarkdownParser


def test_get_version():
    assert MarkdownParser.version == "0.30.2"
