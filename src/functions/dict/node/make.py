from hak.pxyf import f as pxyf

f = lambda name: {'name': name, 'value': None, 'parent': None, 'children': []}

t = lambda: pxyf(
  'foo',
  {'name': 'foo', 'value': None, 'parent': None, 'children': []},
  f
)
