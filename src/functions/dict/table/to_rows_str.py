from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.row.to_str import f as row_to_str
from src.functions.dict.table_and_row_name.to_row import f as row_name_to_row
from src.functions.dict.table.insert_records import f as insert_records
from src.functions.dict.table.make import f as make_table

def f(x):
  rows = [row_name_to_row({'table': x, 'name': n}) for n in x['row_order']]
  return '\n'.join([row_to_str(r) for r in rows])

def t_ab():
  x = insert_records({
    'table': make_table(),
    'records': [
      {'a': 0, 'b': 1},
      {'a': 3, 'b': 4},
      {'a': 6, 'b': 7}
    ]
  })
  y = '\n'.join([
    '|   | 1 |',
    '| 3 | 4 |',
    '| 6 | 7 |',
  ])
  return pxyf(x, y, f, new_line=1)

def t_ac():
  x = insert_records({
    'table': make_table(),
    'records': [
      {'a': 0, 'c': 2},
      {'a': 3, 'c': 5},
      {'a': 6, 'c': 8}
    ]
  })
  y = '\n'.join([
    '|   | 2 |',
    '| 3 | 5 |',
    '| 6 | 8 |',
  ])
  return pxyf(x, y, f, new_line=1)

def t_abc():
  x = insert_records({
    'table': make_table(),
    'records': [
      {'a': 0, 'b': 1, 'c': 2},
      {'a': 3, 'b': 4, 'c': 5},
      {'a': 6, 'b': 7, 'c': 8}
    ]
  })
  y = '\n'.join([
    '|   | 1 | 2 |',
    '| 3 | 4 | 5 |',
    '| 6 | 7 | 8 |',
  ])
  return pxyf(x, y, f, new_line=1)

def t():
  if not t_ab(): return pf('!t_ab')
  if not t_ac(): return pf('!t_ac')
  if not t_abc(): return pf('!t_abc')
  return True
