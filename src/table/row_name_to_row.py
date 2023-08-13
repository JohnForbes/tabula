from hak.pxyz import f as pxyz
from src.table.make import f as make_table
from src.table.insert_records import f as insert_records
from src.cell.make import f as make_cell

f = lambda table, row_name: {
  k: table['cells'][(k, row_name)] for k in table['column_order']
}

def t():
  x = {
    'table': insert_records(make_table(), [
      {'a': 0, 'b': 1, 'c': 2},
      {'a': 3, 'b': 4, 'c': 5},
      {'a': 6, 'b': 7, 'c': 8}
    ]),
    'row_name': 1
  }
  y = {
    'a': make_cell(3),
    'b': make_cell(4),
    'c': make_cell(5),
  }
  z = f(**x)
  return pxyz(x, y, z)
