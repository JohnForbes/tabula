from datetime import date
from hak.one.dict.rate.make import f as make_rate
from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.column.make_from_cells import f as make_column
from src.table.border.add_left_and_right import f as add_left_and_right_borders
from src.table.columns.to_str import f as cols_to_str
from src.table.insert_records import f as insert_records
from src.table.make import f as make_table
from src.table.to_hbar import f as hbar
from src.table.to_header_str import f as head
from src.table.to_rows_str import f as body

get_column_cells_from_table = lambda x, column_name: [
  x['cells'][(column_name, row_identifier)]
  for row_identifier
  in x['row_order']
]

# __str__
# _f = lambda x: '\n'.join([_f(x) for _f in [hbar, head, hbar, body, hbar]])
def f(x):
  columns = [
    make_column(column_name, get_column_cells_from_table(x, column_name))
    for column_name
    in x['column_order']
  ]
  return add_left_and_right_borders(cols_to_str(columns, '|'))

def t_ab():
  x = insert_records(make_table(), [
    {'a': 0, 'b': 1},
    {'a': 3, 'b': 4},
    {'a': 6, 'b': 7}
  ])
  y = '\n'.join([
    '|---|---|',
    '| a | b |',
    '|---|---|',
    '|   | 1 |',
    '| 3 | 4 |',
    '| 6 | 7 |',
    '|---|---|',
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
    '|---|---|',
    '| a | c |',
    '|---|---|',
    '|   | 2 |',
    '| 3 | 5 |',
    '| 6 | 8 |',
    '|---|---|',
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
    '|---|---|---|',
    '| a | b | c |',
    '|---|---|---|',
    '|   | 1 | 2 |',
    '| 3 | 4 | 5 |',
    '| 6 | 7 | 8 |',
    '|---|---|---|',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_date():
  x = insert_records(make_table(), [
    {'date': date(2023, 8, 14), 'b': 1, 'c': 2},
    {'date': date(2023, 8, 14), 'b': 4, 'c': 5},
    {'date': date(2023, 8, 14), 'b': 7, 'c': 8}
  ])
  y = '\n'.join([
    '|------------|---|---|',
    '|       date | b | c |',
    '|------------|---|---|',
    '| 2023-08-14 | 1 | 2 |',
    '| 2023-08-14 | 4 | 5 |',
    '| 2023-08-14 | 7 | 8 |',
    '|------------|---|---|',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_rate():
  x = insert_records(make_table(), [
    {'rate': make_rate(0, 10, {'m': 1}), 'b': 1},
    {'rate': make_rate(1,  9, {'m': 1}), 'b': 4},
    {'rate': make_rate(2,  8, {'m': 1}), 'b': 7},
  ])
  y = '\n'.join([
    '|------|---|',
    '| rate | b |',
    '|------|---|',
    '|  0/1 | 1 |',
    '|  1/9 | 4 |',
    '|  1/4 | 7 |',
    '|------|---|',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t():
  if not t_ab(): return pf('!t_ab')
  if not t_ac(): return pf('!t_ac')
  if not t_abc(): return pf('!t_abc')
  if not t_date(): return pf('!t_date')
  if not t_rate(): return pf('!t_rate')
  return True
