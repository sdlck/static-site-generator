from extract_markdown import extract_title
from markdown_to_html_node import markdown_to_html_node
import os


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as f:
        md = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    
    node = markdown_to_html_node(md)
    html = node.to_html()
    title = extract_title(md)

    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    for object in os.listdir(dir_path_content):
        path = os.path.join(dir_path_content, object)

        if os.path.isfile(path) and path.endswith(".md"):
            with open(template_path, "r") as f:
                template = f.read()

            with open(path, "r") as f:
                md = f.read()
            
            node = markdown_to_html_node(md)
            html = node.to_html()
            title = extract_title(md)

            new_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

            if dest_dir_path:
                os.makedirs(dest_dir_path, exist_ok=True)

            dest_path = os.path.join(dest_dir_path, f"{object[:-3]}.html")
            with open(dest_path, "w") as f:
                f.write(new_template)

        elif os.path.isdir(path):
            generate_pages_recursive(path, template_path, os.path.join(dest_dir_path, object))