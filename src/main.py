from copy_dir import copy_dir
from generate_page import generate_page, generate_pages_recursive

def main():
    copy_dir("static", "public")
    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()