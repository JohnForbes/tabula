from hak.pxyf import f as pxyf

from src.functions.dict.table.insert_record import f as insert_record
from src.functions.dict.table.make import f as make_table

# column_count
f = lambda x: len(x['column_order'])

t = lambda: pxyf(
  insert_record({'table': make_table(), 'record': {'a': 0, 'b': 1, 'c': 2}}),
  3,
  f
)
