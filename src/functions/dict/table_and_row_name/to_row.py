from hak.pxyf import f as pxyf

from src.functions.dict.cell.make import f as make_cell
from src.functions.dict.table.insert_records import f as insert_records
from src.functions.dict.table.make import f as make_table

# table.row_name_to_row
# table, row_name
f = lambda x: {
  k: x['table']['cells'][(k, x['name'])]
  for k
  in x['table']['column_order']
}

def t():
  x = {
    'table': insert_records({
      'table': make_table(),
      'records': [
        {'a': 0, 'b': 1, 'c': 2},
        {'a': 3, 'b': 4, 'c': 5},
        {'a': 6, 'b': 7, 'c': 8}
      ]
    }),
    'name': 1
  }
  y = {
    'a': make_cell({'value': 3, 'field_name': 'a'}),
    'b': make_cell({'value': 4, 'field_name': 'b'}),
    'c': make_cell({'value': 5, 'field_name': 'c'}),
  }
  return pxyf(x, y, f)
