from math import tau
from hak.pxyf import f as pxyf

from src.functions.dict.node.make import f as make_node

# assign_value
def f(node, value):
  node['value'] = value
  return node

def t():
  x = {'node': make_node('foo'), 'value': tau}
  y = {'name': 'foo', 'value': tau, 'parent': None, 'children': []}
  return pxyf(x, y, f)
