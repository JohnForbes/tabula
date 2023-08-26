from hak.pxyf import f as pxyf

from src.functions.dict.cell.make import f as cell
from src.functions.dict.table.insert_records import f as insert_records
from src.functions.dict.table.make import f as table

# table.row_name_to_row
# table, row_name
f = lambda x: {
  k: x['table']['cells'][(k, x['name'])] for k in x['table']['column_order']
}

def t():
  x = {
    'table': insert_records({
      'table': table(),
      'records': [
        {'a': 0, 'b': 1, 'c': 2},
        {'a': 3, 'b': 4, 'c': 5},
        {'a': 6, 'b': 7, 'c': 8}
      ]
    }),
    'name': 1
  }
  y = {
    'a': cell({'value': 3, 'name': 'a'}),
    'b': cell({'value': 4, 'name': 'b'}),
    'c': cell({'value': 5, 'name': 'c'}),
  }
  return pxyf(x, y, f)
