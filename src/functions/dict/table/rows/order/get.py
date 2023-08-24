from hak.pxyf import f as pxyf

from ...insert_records import f as insert_records_into_table
from ...make import f as make_table

# row_order
f = lambda table: table['row_order']

def t():
  x = insert_records_into_table({
    'table': make_table(),
    'records': [
      {'a': 0, 'b': 1, 'c': 2},
      {'a': 3, 'b': 4, 'c': 5},
      {'a': 6, 'b': 7, 'c': 8}
    ]
  })
  y = [0, 1, 2]
  return pxyf(x, y, f)
