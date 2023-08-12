from hak.pxyz import f as pxyz
from src.table.insert_records import f as insert_records
from src.table.make import f as make_table

# from src.column.to_str import f as column_to_str
# from src.row.to_str import f as record_to_str

# __str__
def f(table):
  return '\n'.join([
    '|---|---|---|',
    '| a | b | c |',
    '|---|---|---|',
    '| 0 | 1 | 2 |',
    '| 3 | 4 | 5 |',
    '| 6 | 7 | 8 |',
    '|---|---|---|',
  ])
  # return '\n'.join([
  #   '|---|',
  #   # '| a |',
  #   *[column_to_str(column) for column in table['columns']],
  #   '|---|',
  #   *[record_to_str(record) for record in table['records']],
  #   '|---|',
  # ])

def t():
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
  return pxyz(x, y, z)
