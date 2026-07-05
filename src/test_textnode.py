import unittest
from textnode import TextNode, TextType, text_node_to_html_node

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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
        self.assertEqual(html_node.to_html(), "<i>This is an italic node</i>")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://linknode.local")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.to_html(), '<a href="https://linknode.local">This is a link node</a>')

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://imagenode.local")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.to_html(), '<img src="https://imagenode.local" alt="This is an image node"></img>')