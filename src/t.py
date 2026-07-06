from markdown_to_html_node import markdown_to_html_node

md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

node = markdown_to_html_node(md)

print()
print(node.to_html())
print()
