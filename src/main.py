from textnode import TextType, TextNode

def main():
    text_node = TextNode("test text", TextType.BOLD, "test url")
    print(text_node)

if __name__ == "__main__":
    main()