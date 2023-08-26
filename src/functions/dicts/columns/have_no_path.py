from hak.pf import f as pf
from hak.pxyf import f as pxyf
from src.functions.dict.column.make_from_values import f as column

# condition
f = lambda x: set([c['path'] for c in x]) == {()}

def t_0():
  x = [
    column({'name': 'abc', 'values': [0,  1,   2,    3], 'path': 'numbers'}),
    column({'name': 'ghi', 'values': [0, 10, 200, 3000], 'path': 'numbers'}),
  ]
  y = False
  return pxyf(x, y, f, new_line=1)

def t_1():
  x = [
    column({'name': 'abc', 'values': [0,  1,   2,    3]}),
    column({'name': 'ghi', 'values': [0, 10, 200, 3000]}),
  ]
  y = True
  return pxyf(x, y, f, new_line=1)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  return 1
