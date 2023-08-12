from src.table.make import f as make_table
from hak.pxyz import f as pxyz
from src.cell.make import f as make_cell
from src.table.insert_record import f as insert_record

def f(table, records):
  for r in records:
    table = insert_record(table, r)
  return table

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
    'columns': ['a', 'b', 'c'],
    'rows': [0, 1, 2],
    'cells': {
      ('a', 0): make_cell(0),
      ('b', 0): make_cell(1),
      ('c', 0): make_cell(2),
      ('a', 1): make_cell(3),
      ('b', 1): make_cell(4),
      ('c', 1): make_cell(5),
      ('a', 2): make_cell(6),
      ('b', 2): make_cell(7),
      ('c', 2): make_cell(8),
    }
  }
  z = f(**x)
  return pxyz(x, y, z)
