from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        extracted = extract_markdown_images(node.text)
        if node.text_type == TextType.TEXT and extracted:
            remaining_text = node.text
            for image in extracted:
                split_text = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
                leading_text = split_text[0]
                remaining_text = split_text[1]
                if leading_text:
                    new_nodes.append(TextNode(leading_text, TextType.TEXT))
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        elif node.text:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        extracted = extract_markdown_links(node.text)
        if node.text_type == TextType.TEXT and extracted:
            remaining_text = node.text
            for link in extracted:
                split_text = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
                leading_text = split_text[0]
                remaining_text = split_text[1]
                if leading_text:
                    new_nodes.append(TextNode(leading_text, TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        elif node.text:
            new_nodes.append(node)
    return new_nodes