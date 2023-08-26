from hak.pxyf import f as pxyf

from ...insert_record import f as insert_record
from ...make import f as table

# column_count
f = lambda x: len(x['column_order'])

t = lambda: pxyf(
  insert_record({'table': table(), 'record': {'a': 0, 'b': 1, 'c': 2}}), 3, f
)
