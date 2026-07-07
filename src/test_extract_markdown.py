import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links, extract_title


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://testlink.local)"
        )
        self.assertListEqual([("link", "https://testlink.local")], matches)

    def test_extract_title(self):
        title = extract_title("# Title")
        self.assertEqual(title, "Title")

    def test_extract_title_whitespace(self):
        title = extract_title("#    Title      ")
        self.assertEqual(title, "Title")