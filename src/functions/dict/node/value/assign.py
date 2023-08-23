from math import tau
from hak.pxyz import f as pxyz

from src.functions.dict.node.make import f as make_node

# assign_value
def f(node, value):
  node['value'] = value
  return node

def t():
  x = {'node': make_node('foo'), 'value': tau}
  y = {'name': 'foo', 'value': tau, 'parent': None, 'children': []}
  z = f(**x)
  return pxyz(x, y, z)
