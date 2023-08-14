from hak.pf import f as pf
from hak.pxyz import f as pxyz
from src.column.make import f as make_column

# width
f = lambda x: max(len(x['name']), *[len(str(v)) for v in x['values']])

def t_a():
  x = make_column('apples', [_ for _ in range(100)])
  y = 6
  z = f(x)
  return pxyz(x, y, z)

def t_values_dominant():
  x = make_column('a', [0, 1000, 2, 3])
  y = 4
  z = f(x)
  return pxyz(x, y, z)

def t_name_dominant():
  x = make_column('abc', [0, 1, 2, 3])
  y = 3
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_a(): return pf('!t_a')
  if not t_name_dominant(): return pf('!t_name_dominant')
  if not t_values_dominant(): return pf('!t_values_dominant')
  return True
