from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown: str) -> BlockType:
    if not markdown:
        raise Exception("markdown is required")
    if re.findall(r"^#{1,6} .", markdown):
        return BlockType.HEADING
    if re.findall(r"^```[\s\S]+```$", markdown):
        return BlockType.CODE
    if markdown[0] == ">":
        quote = True
        for line in markdown.split("\n"):
            if line[0] != ">":
               quote = False
               break
        if quote:
            return BlockType.QUOTE
    if len(markdown) > 1 and markdown[:2] == "- ":
        unordered_list = True
        for line in markdown.split("\n"):
            if line[:2] != "- ":
                unordered_list = False
                break
        if unordered_list:
            return BlockType.UNORDERED_LIST
    if len(markdown) > 2 and markdown[:3] == "1. ":
        ordered_list = True
        for i, line in enumerate(markdown.split("\n")):
            if line[:3] != f"{i + 1}. ":
                ordered_list = False
                break
        if ordered_list:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH