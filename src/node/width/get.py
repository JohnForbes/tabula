from datetime import date
from hak.one.dict.is_a import f as is_dict
from hak.one.dict.rate.is_a import f as is_rate
from hak.one.dict.rate.make import f as make_rate
from hak.one.dict.rate.to_str_frac import f as rate_to_str
from hak.one.dict.unit.to_str import f as unit_to_str
from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.node.child.add import f as add_child
from src.node.value.assign import f as assign_value
from src.node.make import f as make_node
from src.nodes.make import f as make_nodes

def _g(k, tree, nodes):
  n = nodes[k]
  if not is_dict(tree[k]) or is_rate(tree[k]):
    assign_value(n, tree[k])
  else:
    for k_child in tree[k].keys():
      add_child(n, nodes[k_child])
      _g(k_child, tree[k], nodes)

def _to_str(x):
  if is_rate(x): return rate_to_str(x)
  return str(x)

# width
def f(node):
  node_name_len = len(node['name'])
  
  children = node['children']
  largest_child_len = max([f(c) for c in children]) if children else 0
  
  value = node['value']
  value_len = len(_to_str(value)) if value else 0
  
  unit = value['unit'] if is_rate(value) else ''
  unit_len = len(unit_to_str(unit))
  
  return max(node_name_len, largest_child_len, value_len, unit_len)

def t_α():
  x = make_node('α')
  y = 1
  z = f(x)
  return pxyz(x, y, z)

def t_α_ab():
  x = make_node('α')
  add_child(x, make_node('a'))
  add_child(x, make_node('b'))
  
  y = 1
  z = f(x)
  return pxyz(x, y, z)

def t_full_no_values():
  x = make_node('α')
  a = make_node('a')
  add_child(x, a)
  
  aa = make_node('aa')
  add_child(a, aa)
  add_child(aa, make_node('aaa'))

  add_child(a, make_node('ab'))

  b = make_node('b')
  add_child(x, b)
  add_child(b, make_node('ba'))
  
  y = 3
  z = f(x)
  return pxyz(x, y, z)

def t_full_with_values():

  d = {
    'α': {
      'a': {'aa': {'aaa': 'Lollipop'}, 'ab': None},
      'b': {'ba': None}
    }
  }

  nodes = make_nodes(d)
  _g('α', d, nodes)

  x = nodes['α']
  y = 8
  z = f(x)
  return pxyz(x, y, z)

def t_prices():
  d = {
    'α': {
      'date': date(2023, 1, 1),
      'prices': {
        'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(2, 4, {'$': 1, 'banana': -1})
      },
    }
  }
  nodes = make_nodes(d)
  _g('α', d, nodes)

  x = nodes['α']
  y = len('2023-01-01')
  z = f(x)
  return pxyz(x, y, z)

def t_rate():
  d = {
    'α': {
      'a': make_rate(1, 4, {'$': 1, 'apple': -1})
    }
  }
  nodes = make_nodes(d)
  _g('α', d, nodes)

  x = nodes['α']
  y = len('$/apple')
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_α(): return pf('!t_α')
  if not t_α_ab(): return pf('!t_α_ab')
  if not t_full_no_values(): return pf('!t_full_no_values')
  if not t_full_with_values(): return pf('!t_full_with_values')
  if not t_prices(): return pf('!t_prices')
  if not t_rate(): return pf('!t_rate')
  return True
