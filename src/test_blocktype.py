import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        markdown = "This is a paragraph"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_heading_1(self):
        markdown = "# This is a heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)

    def test_heading_2(self):
        markdown = "## This is a heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)

    def test_heading_3(self):
        markdown = "### This is a heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)

    def test_heading_4(self):
        markdown = "#### This is a heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)

    def test_heading_5(self):
        markdown = "##### This is a heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)

    def test_heading_6(self):
        markdown = "###### This is a heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)

    def test_not_heading(self):
        markdown = "####### This is not a heading"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_code(self):
        markdown = "```\nThis is code\n```"
        self.assertEqual(block_to_block_type(markdown), BlockType.CODE)

    def test_not_code(self):
        markdown = "```\nThis is not code\n``"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_quote(self):
        markdown = ">this is a quote\n>so is this\n>and this"
        self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)

    def test_not_quote(self):
        markdown = ">this is a quote\n>so is this\nnot this"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        markdown = "- this is an unordered list\n- so is this\n- so is this"
        self.assertEqual(block_to_block_type(markdown), BlockType.UNORDERED_LIST)

    def test_not_unordered_list(self):
        markdown = "- this is an unordered list\n- so is this\nnot this"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        markdown = "1. this is an ordered list\n2. so is this\n3. so is this"
        self.assertEqual(block_to_block_type(markdown), BlockType.ORDERED_LIST)

    def test_not_ordered_list(self):
        markdown = "1. this is an ordered list\n2. so is this\nnot this"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_not_ordered_list_1(self):
        markdown = "1. this is an ordered list\n2. so is this\n4. not this"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)