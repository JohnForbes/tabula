from hak.pxyz import f as pxyz
from src.column.make import f as make_column

# width
f = lambda x: max(len(x['name']), *[len(str(v)) for v in x['values']])

def t():
  x = make_column('apples', [_ for _ in range(100)])
  y = 6
  z = f(x)
  return pxyz(x, y, z)
