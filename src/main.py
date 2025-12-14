from textnode import TextNode
from textnode import TextType

def main():
    test_text = "This is some anchor text"
    test_type = TextType.LINK
    test_url = "https://www.boot.dev"

    test_node = TextNode(test_text, test_type, test_url)
    print(test_node)
    

main()