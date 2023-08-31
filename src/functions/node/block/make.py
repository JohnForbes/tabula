from src.functions.strings.block.hstack import f as hstack
from src.functions.strings.block.vstack import f as vstack
from src.functions.nodes.sort_children_by_nodepath import f as sort_by_nodepath

# _make_block
def f(x):
  top_block = [f' {x.name:^{x.width}} ']
  return (
    vstack([top_block, hstack([c.block for c in sort_by_nodepath(x)])])
    if x.children else
    top_block
  )
