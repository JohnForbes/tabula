from hak.pxyf import f as pxyf

from ...insert_records import f as insert_records
from ...make import f as make_table

# row_count
f = lambda x: len(x['row_order'])

t = lambda: pxyf(
  insert_records({
    'table': make_table(),
    'records': [
      {'a': 0, 'b':  1, 'c':  2},
      {'a': 3, 'b':  4, 'c':  5},
      {'a': 6, 'b':  7, 'c':  8},
      {'a': 9, 'b': 10, 'c': 11}
    ]
  }),
  4,
  f
)
