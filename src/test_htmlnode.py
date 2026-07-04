import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "test value", None, {"href": "https://testurl.local/", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://testurl.local/" target="_blank"')

    def test_props_to_html_no_props(self):
        node = HTMLNode("a", "test value", None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("a", "test value", None, {"href": "https://testurl.local/", "target": "_blank"})
        self.assertEqual(node.__repr__(), "HTMLNode(a, test value, None, {'href': 'https://testurl.local/', 'target': '_blank'})")