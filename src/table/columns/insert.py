from src.table.make import f as make_table
from copy import deepcopy as cp
from hak.pxyz import f as pxyz

# insert_column
f = lambda table, column: make_table(
  columns=cp(table['columns']) + [column],
  rows=cp(table['rows'])
)

def t():
  x = {
    'table': make_table(columns=['a', 'b']),
    'column': 'c'
  }
  y = make_table(columns=['a', 'b', 'c'])
  z = f(**x)
  return pxyz(x, y, z)
