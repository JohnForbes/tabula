from hak.one.dict.is_a import f as is_dict
from hak.pf import f as pf
from hak.pxyz import f as pxyz

def f(x):
  if not is_dict(x): return False
  if 'name' not in x: return False
  if 'values' not in x: return False
  return True

def t_0():
  x = {'a': '...', 'b': '...'}
  y = 0
  z = f(x)
  return pxyz(x, y, z)

def t_1():
  x = {'name': 'foo', 'values': [0, 1, 2]}
  y = 1
  z = f(x)
  return pxyz(x, y, z)


def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  return 1
