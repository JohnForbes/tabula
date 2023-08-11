from hak.pf import f as pf
from hak.pxyz import f as pxyz
from src.cell.make import f as make_cell

f = lambda x: str(x['value'])

def t_0():
  x = {'value': 'a'}
  y = 'a'
  z = f(make_cell(**x))
  return pxyz(x, y, z)

def t():
  if not t_0(): return pf('t_0 failed')
  return True
