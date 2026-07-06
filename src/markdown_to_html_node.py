from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown: str) -> HTMLNode:
    nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        text_nodes = text_to_textnodes(block)
        child_nodes = []
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                for text_node in text_nodes:
                    child_nodes.append(text_node_to_html_node(text_node))
                nodes.append(ParentNode("p", child_nodes))
    return ParentNode("div", nodes)