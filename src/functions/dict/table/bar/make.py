from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.table.insert_records import f as insert_records
from src.functions.dict.table.make import f as make_table

f = lambda table: (
  '|-'+'-|-'.join(['-'*len(f'{c}') for c in table['column_order']])+'-|'
)

# make_bar
# f = lambda x: "|-"+'-|-'.join(['-'*x['widths'][k] for k in x['names']])+"-|"

def t_ac():
  x = insert_records({
    'table': make_table(),
    'records': [
      {'a': 0, 'c': 2},
      {'a': 3, 'c': 5},
      {'a': 6, 'c': 8}
    ]
  })
  y = '|---|---|'
  return pxyf(x, y, f, new_line=1)

def t_abc():
  x = insert_records({
    'table': make_table(),
    'records': [
      {'a': 0, 'b': 1, 'c': 2},
      {'a': 3, 'b': 4, 'c': 5},
      {'a': 6, 'b': 7, 'c': 8}
    ]
  })
  y = '|---|---|---|'
  return pxyf(x, y, f, new_line=1)

def t():
  if not t_ac(): return pf('!t_ac')
  if not t_abc(): return pf('!t_abc')
  return 1
