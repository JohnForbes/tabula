from src.table.make import f as make_table
from hak.pxyz import f as pxyz
from hak.one.list.append_if_not_present import f as append_if_not_present
from src.cell.make import f as make_cell

def f(table, record):
  max_row_identifier = max(table['row_order']) if table['row_order'] else -1
  row_identifier = max_row_identifier+1
  table['row_order'] = table['row_order'] + [row_identifier]

  for (k, v) in record.items():
    table['column_order'] = append_if_not_present(table['column_order'], k)
    table['cells'][(k, row_identifier)] = make_cell(v, k)

  return table

def t():
  x = {'table': make_table(), 'record': {'a': 0, 'b': 1, 'c': 2}}
  y = {
    'column_order': ['a', 'b', 'c'],
    'row_order': [0],
    'cells': {
      ('a', 0): make_cell(0, 'a'),
      ('b', 0): make_cell(1, 'b'),
      ('c', 0): make_cell(2, 'c')
    }
  }
  z = f(**x)
  return pxyz(x, y, z)
