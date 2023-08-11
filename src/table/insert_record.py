from src.table.make import f as make_table
from hak.pxyz import f as pxyz
from hak.one.list.append_if_not_present import f as append_if_not_present
from src.cell.make import f as make_cell

def f(table, record):
  last_row_identifier = table['rows'][-1] if table['rows'] else -1
  row_identifier = last_row_identifier+1
  table['rows'] = table['rows'] + [row_identifier]

  for (k, v) in record.items():
    table['columns'] = append_if_not_present(table['columns'], k)
    table['cells'][(k, row_identifier)] = make_cell(v)

  return table

def t():
  x = {
    'table': make_table(),
    'record': {'a': 0, 'b': 1, 'c': 2}
  }
  y = {
    'columns': ['a', 'b', 'c'],
    'rows': [0],
    'cells': {
      ('a', 0): make_cell(0),
      ('b', 0): make_cell(1),
      ('c', 0): make_cell(2)
    }
  }
  z = f(**x)
  return pxyz(x, y, z)
