from hak.pf import f as pf
from hak.one.list.append_if_not_present import f as append_if_not_present

from src.functions.dict.node.make import f as make_node

# add_child
def f(node, child):
  node['children'] = append_if_not_present(node['children'], child)
  child['parent'] = node
  return node, child

def t():
  node = make_node('foo')
  child = make_node('bar')
  f(node, child)
  if not len(node['children']): return pf("not len(x['node']['children'])")
  if not (node['children'][0]['name'] == 'bar'): return pf('!A')
  if not (child['parent']['name'] == 'foo'): return pf('!B')
  if not (child['parent']['children'][0]['name'] == 'bar'): return pf('!C')
  return True
