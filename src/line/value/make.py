from hak.pxyz import f as pxyz
from hak.pf import f as pf

f = lambda v, w: f' {v:>{w}} '

def t_int():
  x = {'v': 12, 'w': 10}
  y = '         12 '
  z = f(**x)
  return pxyz(x, y, z)

def t():
  if not t_int(): return pf('!t_int')
  return True
