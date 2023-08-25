from hak.pxyf import f as pxyf

from .insert_records import f as insert_records
from .make import f as table

# table_to_header_str
f = lambda table: '| '+' | '.join([f'{c}' for c in table['column_order']])+' |'
def t():
  x = insert_records({
    'table': table(),
    'records': [
      {'a': 0, 'b': 1, 'c': 2},
      {'a': 3, 'b': 4, 'c': 5},
      {'a': 6, 'b': 7, 'c': 8}
    ]
  })
  y = '| a | b | c |'
  return pxyf(x, y, f)
