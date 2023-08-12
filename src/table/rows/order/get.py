from src.table.make import f as make_table
from src.table.insert_records import f as insert_records_into_table
from hak.pxyz import f as pxyz

# row_order
f = lambda table: table['rows']

def t():
  x = {
    'table': insert_records_into_table(make_table(), [
      {'a': 0, 'b': 1, 'c': 2},
      {'a': 3, 'b': 4, 'c': 5},
      {'a': 6, 'b': 7, 'c': 8}
    ])
  }
  y = [0, 1, 2]
  z = f(**x)
  return pxyz(x, y, z)
