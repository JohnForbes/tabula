from src.functions.strings.block.to_str import f as block_to_str
from src.functions.node.block.make import f as make_block
from src.functions.node.width.get import f as get_width
from hak.pf import f as pf
# from src.classes.table import Table

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

# def t__init():
#   x = {
#     'name': 'node_name',
#     'table': Table(),
#   }
#   return 0

def t__str(): return 0
def t_add_child(): return 0
def t_add_children(): return 0
def t_block(): return 0
def t_level(): return 0
def t_width(): return 0

def t():
  # if not t__init(): return pf('!t__init')
  if not t__str(): return pf('!t__str')
  if not t_add_child(): return pf('!t_add_child')
  if not t_add_children(): return pf('!t_add_children')
  if not t_block(): return pf('!t_block')
  if not t_level(): return pf('!t_level')
  if not t_width(): return pf('!t_width')
  return 1
