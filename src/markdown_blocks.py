def markdown_to_blocks(markdown):
    list_of_blocks = []

    for block in markdown.split("\n\n"):
        if block == "":
            continue
        
        list_of_blocks.append(block.strip())
    
    return list_of_blocks
