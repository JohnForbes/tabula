from datetime import date
from hak.one.dict.rate.is_a import f as is_rate
from hak.one.dict.rate.make import f as make_rate
from hak.one.dict.rate.to_str_frac import f as rate_to_str
from hak.one.dict.unit.to_str import f as unit_to_str
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ....dict.node.child.add import f as add_child
from ....dict.node.make import f as make_node
from ....dict.records_and_name.make_node_tree import f as build_tree
from ....dicts.nodes.make import f as make_nodes

_to_str = lambda x: rate_to_str(x) if is_rate(x) else str(x)

# width
f = lambda node: max(
  len(node['name']),
  sum([f(c) for c in node['children']]) if node['children'] else 0,
  len(_to_str(node['value'])) if node['value'] else 0,
  len(unit_to_str(node['value']['unit'] if is_rate(node['value']) else ''))
)

t_α = lambda: pxyf(make_node('α'), 1, f)

def t_α_ab():
  x = make_node('α')
  add_child(x, make_node('a'))
  add_child(x, make_node('b'))
  return pxyf(x, 2, f)

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
  
  return pxyf(x, 7, f)

def t_full_with_values():
  d = {
    'α': {
      'a': {'aa': {'aaa': 'Lollipop'}, 'ab': None},
      'b': {'ba': None}
    }
  }
  nodes = build_tree('α', d)
  x = nodes['α']
  return pxyf(x, 12, f)

def t_prices():
  d = {
    'date': date(2023, 1, 1),
    'prices': {
      'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
      'bananas': make_rate(2, 4, {'$': 1, 'banana': -1})
    },
  }
  nodes = build_tree('prices', d)
  x = nodes['prices']
  return pxyf(x, len('$/apple')+len('$/banana'), f)

def t_rate():
  d = {'a': make_rate(1, 4, {'$': 1, 'apple': -1})}
  nodes = build_tree('a', d)
  x = nodes['a']
  return pxyf(x, len('$/apple'), f)

def t():
  if not t_α(): return pf('!t_α')
  if not t_α_ab(): return pf('!t_α_ab')
  if not t_full_no_values(): return pf('!t_full_no_values')
  if not t_full_with_values(): return pf('!t_full_with_values')
  if not t_prices(): return pf('!t_prices')
  if not t_rate(): return pf('!t_rate')
  return True
