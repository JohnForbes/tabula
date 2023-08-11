from src.table.make import f as make_table
from hak.pxyz import f as pxyz

# row_count
f = lambda x: len(x['rows'])

def t():
  x = make_table(columns=['a', 'b', 'c'], rows=[0, 1, 2, 3])
  y = 4
  z = f(x)
  return pxyz(x, y, z)
