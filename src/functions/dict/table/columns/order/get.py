from hak.pxyf import f as pxyf

from ...insert_record import f as insert_record
from ...make import f as table

# column_order
f = lambda x: x['column_order']

t = lambda: pxyf(
  insert_record({'table': table(), 'record': {'a': 0, 'b': 1, 'c': 2}}),
  ['a', 'b', 'c'],
  f
)
