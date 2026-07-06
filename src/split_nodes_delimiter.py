from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    if not delimiter:
        raise Exception("delimiter is required")
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise Exception("missing closing delimiter")
            for i, text in enumerate(split_text):
                if text == "":
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(text, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(text, text_type))
        else:
            new_nodes.append(node)
    return new_nodes