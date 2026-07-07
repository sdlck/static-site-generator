import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
# This is a heading

## so is this

### and this

#### and this

##### and this

###### and this
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1><h2>so is this</h2><h3>and this</h3><h4>and this</h4><h5>and this</h5><h6>and this</h6></div>"
        )

    def test_quote(self):
        md = """
>This is a block quote
> so is this
>and this
>and this **with** some _stuff_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a block quote\nso is this\nand this\nand this <b>with</b> some <i>stuff</i></blockquote></div>"
        )

    def test_unordered_list(self):
        md = """
- This is an unordered list
- so is this
- and this
- and this **with** some _stuff_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an unordered list</li><li>so is this</li><li>and this</li><li>and this <b>with</b> some <i>stuff</i></li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. This is an ordered list
2. so is this
3. and this
4. and this **with** some _stuff_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an ordered list</li><li>so is this</li><li>and this</li><li>and this <b>with</b> some <i>stuff</i></li></ol></div>"
        )