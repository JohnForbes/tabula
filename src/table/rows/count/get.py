from hak.pxyz import f as pxyz

from src.table.insert_records import f as insert_records
from src.table.make import f as make_table

# row_count
f = lambda x: len(x['row_order'])

def t():
  x = insert_records(make_table(), [
    {'a': 0, 'b':  1, 'c':  2},
    {'a': 3, 'b':  4, 'c':  5},
    {'a': 6, 'b':  7, 'c':  8},
    {'a': 9, 'b': 10, 'c': 11}
  ])
  y = 4
  z = f(x)
  return pxyz(x, y, z)
