from src.table.make import f as make_table
from hak.pxyz import f as pxyz

# column_count
f = lambda x: len(x['columns'])

def t():
  x = make_table(columns=['a', 'b', 'c'])
  y = 3
  z = f(x)
  return pxyz(x, y, z)
