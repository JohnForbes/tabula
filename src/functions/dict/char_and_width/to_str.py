from hak.pf import f as pf
from hak.pxyz import f as pxyz

# h
# f = lambda c, w: c*(w+2)
f = lambda x: x['char']*(x['width']+2)

def t_minus_3():
  x = {'char': '-', 'width': 3}
  y = '-----'
  z = f(x)
  return pxyz(x, y, z)

def t_minus_4():
  x = {'char': '-', 'width': 4}
  y = '------'
  z = f(x)
  return pxyz(x, y, z)

def t_space_4():
  x = {'char': ' ', 'width': 4}
  y = '      '
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_minus_3(): return pf('!t_minus_3')
  if not t_minus_4(): return pf('!t_minus_4')
  if not t_space_4(): return pf('!t_space_4')
  return True
