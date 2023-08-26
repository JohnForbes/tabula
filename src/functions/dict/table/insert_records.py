from hak.pxyf import f as pxyf

from ..cell.make import f as make_cell
from .insert_record import f as insert_record
from .make import f as make_table

f = lambda x: (
  f({
    'table': insert_record({'table': x['table'], 'record': x['records'][0]}),
    'records': x['records'][1:]
  })
  if x['records'] else
  x['table']
)

def t():
  x = {
    'table': make_table(),
    'records': [
      {'a': 0, 'b': 1, 'c': 2},
      {'a': 3, 'b': 4, 'c': 5},
      {'a': 6, 'b': 7, 'c': 8}
    ]
  }
  y = {
    'column_order': ['a', 'b', 'c'],
    'row_order': [0, 1, 2],
    'cells': {
      ('a', 0): make_cell({'value': 0, 'name': 'a'}),
      ('b', 0): make_cell({'value': 1, 'name': 'b'}),
      ('c', 0): make_cell({'value': 2, 'name': 'c'}),
      ('a', 1): make_cell({'value': 3, 'name': 'a'}),
      ('b', 1): make_cell({'value': 4, 'name': 'b'}),
      ('c', 1): make_cell({'value': 5, 'name': 'c'}),
      ('a', 2): make_cell({'value': 6, 'name': 'a'}),
      ('b', 2): make_cell({'value': 7, 'name': 'b'}),
      ('c', 2): make_cell({'value': 8, 'name': 'c'}),
    }
  }
  return pxyf(x, y, f, new_line=1)
