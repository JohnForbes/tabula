from hak.one.string.is_a import f as is_str
from hak.pxyz import f as pxyz
from hak.pf import f as pf

def f(x): return is_str(x) and '\n' not in x

def t_false():
  x = 0
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_true():
  x = 'abc'
  y = True
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_false(): return pf('!t_false')
  if not t_true(): return pf('!t_true')
  return True
