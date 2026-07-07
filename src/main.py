from copy_dir import copy_dir
from generate_page import generate_page, generate_pages_recursive
import sys


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_dir("static", "docs")

    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()