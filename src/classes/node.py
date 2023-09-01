from hak.pf import f as pf
from src.functions.ints.cell_value_widths.to_aggregate_width import f as aw
from src.functions.nodes.sort_children_by_nodepath import f as sort_by_nodepath
from src.functions.strings.block.hstack import f as hstack
from src.functions.strings.block.vstack import f as vstack
# from src.classes.table import Table

def make_block(x):
  top_block = [f' {x.name:^{x.width}} ']
  return (
    vstack([top_block, hstack([c.block for c in sort_by_nodepath(x)])])
    if x.children else
    top_block
  )

get_width = lambda node: max(
  len(node.name),
  aw([c.width for c in node.children]),
  (
    node.table.get_column(node.nodepath).width
    if (node.nodepath, 0) in node.table.cells else
    0
  )
)

class Node:
  def __init__(self, name, table):
    self.name = name
    self.children = set()
    self.nodepath = tuple([name])
    self.table = table

  def add_child(self, child):
    self.children.add(child)
    child.nodepath = tuple(list(self.nodepath)+ list(child.nodepath))

  block = property(make_block)
  width = property(get_width)

f = lambda name, table: Node(name, table)

def t__init():
  from importlib import import_module
  _Table = import_module('src.classes.table').Table
  _table = _Table()
  node = Node('node_name', _table)
  if node.name != 'node_name': return pf("node.name != 'node_name'")
  if node.children != set(): return pf("node.children != set()")
  if node.nodepath != tuple(['node_name']):
    return pf("node.nodepath != tuple(['node_name'])")
  if node.table != _table: return pf("node.table != _table")
  return 1

def t__str(): return 0
def t_add_child(): return 0
def t_add_children(): return 0
def t_block(): return 0
def t_level(): return 0
def t_width(): return 0

def t():
  if not t__init(): return pf('!t__init')
  # if not t__str(): return pf('!t__str')
  # if not t_add_child(): return pf('!t_add_child')
  # if not t_add_children(): return pf('!t_add_children')
  # if not t_block(): return pf('!t_block')
  # if not t_level(): return pf('!t_level')
  # if not t_width(): return pf('!t_width')
  return 1
