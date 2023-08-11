from src.table.make import f as make_table
from hak.pxyz import f as pxyz

# column_order
f = lambda x: x['columns']

def t():
  x = make_table(columns=['a', 'b', 'c'])
  y = ['a', 'b', 'c']
  z = f(x)
  return pxyz(x, y, z)
