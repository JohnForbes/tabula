from src.table.make import f as make_table
from hak.pxyz import f as pxyz
from src.cell.make import f as make_cell
from src.table.insert_record import f as insert_record

f = lambda table, records: (
  f(insert_record(table, records[0]), records[1:]) if records else table
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
      ('a', 0): make_cell(0, 'a'),
      ('b', 0): make_cell(1, 'b'),
      ('c', 0): make_cell(2, 'c'),
      ('a', 1): make_cell(3, 'a'),
      ('b', 1): make_cell(4, 'b'),
      ('c', 1): make_cell(5, 'c'),
      ('a', 2): make_cell(6, 'a'),
      ('b', 2): make_cell(7, 'b'),
      ('c', 2): make_cell(8, 'c'),
    }
  }
  z = f(**x)
  return pxyz(x, y, z, new_line=1)
