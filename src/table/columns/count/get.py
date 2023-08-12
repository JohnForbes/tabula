from hak.pxyz import f as pxyz

from src.table.insert_record import f as insert_record
from src.table.make import f as make_table

# column_count
f = lambda x: len(x['column_order'])

def t():
  x = insert_record(make_table(), {'a': 0, 'b': 1, 'c': 2})
  y = 3
  z = f(x)
  return pxyz(x, y, z)
