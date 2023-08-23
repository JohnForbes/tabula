from hak.one.dict.get_all_keys_and_subkeys_as_set import f as get_key_set
from hak.pxyf import f as pxyf

from src.functions.dict.node.make import f as make_node

f = lambda x: {k: make_node(k) for k in get_key_set(x, set()) | set('α')}

def t():
  x = {'a': {'aa': {'aaa': 'Lollipop'}, 'ab': None}, 'b': {'ba': None}}
  y = {
    'a': {'name': 'a', 'value': None, 'parent': None, 'children': []},
    'aa': {'name': 'aa', 'value': None, 'parent': None, 'children': []},
    'aaa': {'name': 'aaa', 'value': None, 'parent': None, 'children': []},
    'ab': {'name': 'ab', 'value': None, 'parent': None, 'children': []},
    'b': {'name': 'b', 'value': None, 'parent': None, 'children': []},
    'ba': {'name': 'ba', 'value': None, 'parent': None, 'children': []},
    'α': {'name': 'α', 'value': None, 'parent': None, 'children': []},
  }
  return pxyf(x, y, f)
