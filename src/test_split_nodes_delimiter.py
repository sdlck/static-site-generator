import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("this is text with a **bold** word", TextType.TEXT)
        node1 = TextNode("this is text with a ", TextType.TEXT)
        node2 = TextNode("bold", TextType.BOLD)
        node3 = TextNode(" word", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [node1, node2, node3])

    def test_italic(self):
        node = TextNode("this is text with an _italic_ word", TextType.TEXT)
        node1 = TextNode("this is text with an ", TextType.TEXT)
        node2 = TextNode("italic", TextType.ITALIC)
        node3 = TextNode(" word", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "_", TextType.ITALIC), [node1, node2, node3])

    def test_code(self):
        node = TextNode("this is text with a `code block` word", TextType.TEXT)
        node1 = TextNode("this is text with a ", TextType.TEXT)
        node2 = TextNode("code block", TextType.CODE)
        node3 = TextNode(" word", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), [node1, node2, node3])