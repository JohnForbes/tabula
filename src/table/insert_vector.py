from src.table.make import f as make_table
from hak.pxyz import f as pxyz
from src.cell.make import f as make_cell

def f(table, vector):
  name = vector['name']
  values = vector['values']

  result_table = make_table()
  result_table['column_order'] = table['column_order'] + [name]

  row_identifier = max(table['row_order']) if table['row_order'] else -1
  result_table['row_order'] = table['row_order']

  for v in values:
    row_identifier = row_identifier+1
    result_table['row_order'] = result_table['row_order'] + [row_identifier]
    result_table['cells'][(name, row_identifier)] = make_cell(v)

  return result_table

def t():
  x = {
    'table': make_table(),
    'vector': {
      'name': 'd',
      'values': [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    }
  }
  y = {
    'column_order': ['d'],
    'row_order': [_ for _ in range(10)],
    'cells': {('d', _): make_cell(_/10) for _ in range(10)}
  }
  z = f(**x)
  return pxyz(x, y, z)
