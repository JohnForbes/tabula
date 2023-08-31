from src.functions.blocks.get_max_height import f as get_max_block_height

def f(blocks):
  max_block_height = get_max_block_height(blocks)
  for block in blocks:
    while len(block) < max_block_height:
      block.append(' '*len(block[0]))
  return blocks
