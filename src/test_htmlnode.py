import unittest
from htmlnode import HTMLNode, LeafNode

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

class TestLeafNode(unittest.TestCase):
    def test_props_to_html(self):
        node = LeafNode("a", "test value", {"href": "https://testurl.local/", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://testurl.local/" target="_blank"')

    def test_props_to_html_no_props(self):
        node = LeafNode("a", "test value", None)
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = LeafNode("a", "test value", {"href": "https://testurl.local/", "target": "_blank"})
        self.assertEqual(node.__repr__(), "HTMLNode(a, test value, {'href': 'https://testurl.local/', 'target': '_blank'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_href(self):
        node = LeafNode("a", "test value", {"href": "https://testurl.local/", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://testurl.local/" target="_blank">test value</a>')