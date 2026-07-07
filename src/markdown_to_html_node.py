from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def paragraph_to_html_node(block: str) -> ParentNode:
    text_nodes = text_to_textnodes(block.replace("\n", " "))
    child_nodes = []
    for text_node in text_nodes:
        child_nodes.append(text_node_to_html_node(text_node))
    return ParentNode("p", child_nodes)

def heading_to_html_node(block: str) -> ParentNode:
    stripped = block.lstrip("#")
    count = len(block) - len(stripped)
    text_nodes = text_to_textnodes(stripped[1:])
    child_nodes = []
    for text_node in text_nodes:
        child_nodes.append(text_node_to_html_node(text_node))
    return ParentNode(f"h{count}", child_nodes)

def code_to_html_node(block: str) -> ParentNode:
    stripped = block[4:-3]
    text_node = TextNode(stripped, TextType.CODE)
    return ParentNode("pre", [text_node_to_html_node(text_node)])

def quote_to_html_node(block: str) -> ParentNode:
    split = block.split("\n")
    joined = []
    for line in split:
        joined.append(line.lstrip(">").lstrip(" "))
    stripped = "\n".join(joined)
    child_nodes = []
    text_nodes = text_to_textnodes(stripped)
    for text_node in text_nodes:
        child_nodes.append(text_node_to_html_node(text_node))
    return ParentNode("blockquote", child_nodes)

def unordered_list_to_html_node(block: str) -> ParentNode:
    split = block.split("\n")
    child_nodes = []
    for line in split:
        stripped = line[2:]
        text_nodes = text_to_textnodes(stripped)
        grandchild_nodes = []
        for text_node in text_nodes:
            grandchild_nodes.append(text_node_to_html_node(text_node))
        child_nodes.append(ParentNode("li", grandchild_nodes))
    return ParentNode("ul", child_nodes)

def ordered_list_to_html_node(block: str) -> ParentNode:
    split = block.split("\n")
    child_nodes = []
    for line in split:
        stripped = line.split(" ", 1)[1]
        text_nodes = text_to_textnodes(stripped)
        grandchild_nodes = []
        for text_node in text_nodes:
            grandchild_nodes.append(text_node_to_html_node(text_node))
        child_nodes.append(ParentNode("li", grandchild_nodes))
    return ParentNode("ol", child_nodes)

def markdown_to_html_node(markdown: str) -> ParentNode:
    nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                nodes.append(paragraph_to_html_node(block))
            case BlockType.HEADING:
                nodes.append(heading_to_html_node(block))
            case BlockType.CODE:
                nodes.append(code_to_html_node(block))
            case BlockType.QUOTE:
                nodes.append(quote_to_html_node(block))
            case BlockType.UNORDERED_LIST:
                nodes.append(unordered_list_to_html_node(block))
            case BlockType.ORDERED_LIST:
                nodes.append(ordered_list_to_html_node(block))
    return ParentNode("div", nodes)