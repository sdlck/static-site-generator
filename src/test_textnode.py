import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node1)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node1)

    def test_not_eq_texttype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node1)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://testurl.local/")
        node1 = TextNode("This is a text node", TextType.BOLD, "https://differenturl.local")
        self.assertNotEqual(node, node1)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node1 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node1)
