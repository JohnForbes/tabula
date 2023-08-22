from hak.pxyz import f as pxyz

f = lambda name: {'name': name, 'value': None, 'parent': None, 'children': []}

def t():
  x = 'foo'
  y = {'name': 'foo', 'value': None, 'parent': None, 'children': []}
  z = f(x)
  return pxyz(x, y, z)
