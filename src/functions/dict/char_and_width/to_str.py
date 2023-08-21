from hak.pxyz import f as pxyz

# h
# f = lambda c, w: c*(w+2)
f = lambda x: x['char']*(x['width']+2)

def t():
  x = {
    'char': '-',
    'width': 4
  }
  y = '------'
  z = f(x)
  return pxyz(x, y, z)
