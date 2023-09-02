from hak.pf import f as pf
from hak.many.numbers.ints.cell_value_widths.to_aggregate_width import f as aw

from src.functions.nodes.sort_children_by_nodepath import f as sort_by_nodepath
from src.functions.strings.block.hstack import f as hstack
from src.functions.strings.block.vstack import f as vstack

class Node:
  def __init__(self, name, table):
    self.name = name
    self.children = set()
    self.nodepath = tuple([name])
    self.table = table

  def add_child(self, child):
    self.children.add(child)
    child.nodepath = tuple(list(self.nodepath)+ list(child.nodepath))

  def _make_block(x):
    top_block = [f' {x.name:^{x.width}} ']
    return (
      vstack([top_block, hstack([c.block for c in sort_by_nodepath(x)])])
      if x.children else
      top_block
    )

  block = property(_make_block)

  _get_width = lambda node: max(
    len(node.name),
    aw([c.width for c in node.children]),
    (
      node.table.get_column(node.nodepath).width
      if (node.nodepath, 0) in node.table.cells else
      0
    )
  )

  width = property(_get_width)

f = lambda name, table: Node(name, table)

def t_node__init(T):
  _table = T()
  node = Node('node_name', _table)
  if node.name != 'node_name': return pf("node.name != 'node_name'")
  if node.children != set(): return pf("node.children != set()")
  if node.nodepath != tuple(['node_name']):
    return pf("node.nodepath != tuple(['node_name'])")
  if node.table != _table: return pf("node.table != _table")
  return 1

def t_node__str(T): return 0
def t_node_add_child(T): return 0
def t_node_add_children(T): return 0
def t_node_block(T): return 0
def t_node_level(T): return 0
def t_node_width(T): return 0

def t():
  from importlib import import_module
  T = import_module('src.classes.table').Table
  if not t_node__init(T): return pf('!t_node__init')
  # if not t_node__str(T): return pf('!t_node__str')
  # if not t_node_add_child(T): return pf('!t_node_add_child')
  # if not t_node_add_children(T): return pf('!t_node_add_children')
  # if not t_node_block(T): return pf('!t_node_block')
  # if not t_node_level(T): return pf('!t_node_level')
  # if not t_node_width(T): return pf('!t_node_width')
  return 1
