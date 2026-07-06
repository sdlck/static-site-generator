def markdown_to_blocks(markdown: str) -> list[str]:
     return [b for b in (block.strip() for block in markdown.split("\n\n")) if b]