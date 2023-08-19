from hak.pxyz import f as pxyz
from hak.pf import f as pf
from hak.one.list.is_a import f as is_list
from hak.one.string.is_a import f as is_string

def f(x):
  if not is_list(x): return pf('!is_list')
  for item in x:
    if not is_string(item): return False
  return all([j == len(x[0]) for j in [len(x_i) for x_i in x]])

def t_true():
  x = ['111' for _ in range(4)]
  y = True
  z = f(x)
  return pxyz(x, y, z)

def t_false():
  x = ['111', '1111', '11', '111']
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_true(): return pf('!t_true')
  if not t_false(): return pf('!t_false')
  return True
