from hak.pxyz import f as pxyz
from src.table.insert_records import f as insert_records
from src.table.make import f as make_table
from hak.pf import f as pf
from src.column.to_str import f as column_to_str
# from src.row.to_str import f as record_to_str
from src.row.to_str import f as row_to_str
from src.table.to_header_str import f as table_to_header_str

# __str__
def f(table):
  return '\n'.join([
    '|---|---|',
    # '| a | b |',
    table_to_header_str(table),
    '|---|---|',
    # *[
    #   '| ' + row_to_str(row) + ' |'
    #   for row
    #   in 
    # ],
    '| 0 | 1 |',
    '| 3 | 4 |',
    '| 6 | 7 |',
    '|---|---|',
  ])
  # return '\n'.join([
  #   '|---|',
  #   # '| a |',
  #   *[column_to_str(column) for column in table['column_order']],
  #   '|---|',
  #   *[record_to_str(record) for record in table['records']],
  #   '|---|',
  # ])

def t_abc():
  x = {
    'table': insert_records(make_table(), [
      {'a': 0, 'b': 1, 'c': 2},
      {'a': 3, 'b': 4, 'c': 5},
      {'a': 6, 'b': 7, 'c': 8}
    ])
  }
  y = '\n'.join([
    '|---|---|---|',
    '| a | b | c |',
    '|---|---|---|',
    '| 0 | 1 | 2 |',
    '| 3 | 4 | 5 |',
    '| 6 | 7 | 8 |',
    '|---|---|---|',
  ])
  z = f(**x)
  return pxyz(x, y, z, new_line=1)

def t_ab():
  x = {
    'table': insert_records(make_table(), [
      {'a': 0, 'b': 1},
      {'a': 3, 'b': 4},
      {'a': 6, 'b': 7}
    ])
  }
  y = '\n'.join([
    '|---|---|',
    '| a | b |',
    '|---|---|',
    '| 0 | 1 |',
    '| 3 | 4 |',
    '| 6 | 7 |',
    '|---|---|',
  ])
  z = f(**x)
  return pxyz(x, y, z, new_line=1)

def t_ac():
  x = {
    'table': insert_records(make_table(), [
      {'a': 0, 'c': 1},
      {'a': 3, 'c': 4},
      {'a': 6, 'c': 7}
    ])
  }
  y = '\n'.join([
    '|---|---|',
    '| a | c |',
    '|---|---|',
    '| 0 | 2 |',
    '| 3 | 5 |',
    '| 6 | 8 |',
    '|---|---|',
  ])
  z = f(**x)
  return pxyz(x, y, z, new_line=1)

def t():
  if not t_ab(): return pf('!t_ab')
  # if not t_ac(): return pf('!t_ac')
  # if not t_abc(): return pf('!t_abc')
  return True
