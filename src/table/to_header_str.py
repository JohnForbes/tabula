from src.table.insert_records import f as insert_records
from src.table.make import f as make_table
from hak.pxyz import f as pxyz

# table_to_header_str
f = lambda table: '| '+' | '.join([f'{c}' for c in table['column_order']])+' |'
def t():
  x = {
    'table': insert_records(make_table(), [
      {'a': 0, 'b': 1, 'c': 2},
      {'a': 3, 'b': 4, 'c': 5},
      {'a': 6, 'b': 7, 'c': 8}
    ])
  }
  y = '| a | b | c |'
  z = f(**x)
  return pxyz(x, y, z)
