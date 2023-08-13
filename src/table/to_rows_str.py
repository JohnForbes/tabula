from src.table.row_name_to_row import f as row_name_to_row
from src.row.to_str import f as row_to_str
from hak.pf import f as pf
from hak.pxyz import f as pxyz
from src.table.insert_records import f as insert_records
from src.table.make import f as make_table

def f(x):
  rows = [row_name_to_row(x, row_name) for row_name in x['row_order']]
  return '\n'.join([row_to_str(r) for r in rows])

def t_ab():
  x = insert_records(make_table(), [
    {'a': 0, 'b': 1},
    {'a': 3, 'b': 4},
    {'a': 6, 'b': 7}
  ])
  y = '\n'.join([
    '| 0 | 1 |',
    '| 3 | 4 |',
    '| 6 | 7 |',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_ac():
  x = insert_records(make_table(), [
    {'a': 0, 'c': 2},
    {'a': 3, 'c': 5},
    {'a': 6, 'c': 8}
  ])
  y = '\n'.join([
    '| 0 | 2 |',
    '| 3 | 5 |',
    '| 6 | 8 |',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_abc():
  x = insert_records(make_table(), [
    {'a': 0, 'b': 1, 'c': 2},
    {'a': 3, 'b': 4, 'c': 5},
    {'a': 6, 'b': 7, 'c': 8}
  ])
  y = '\n'.join([
    '| 0 | 1 | 2 |',
    '| 3 | 4 | 5 |',
    '| 6 | 7 | 8 |',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t():
  if not t_ab(): return pf('!t_ab')
  if not t_ac(): return pf('!t_ac')
  if not t_abc(): return pf('!t_abc')
  return True
