from src.table.insert_records import f as insert_records
from src.table.make import f as make_table
from hak.pxyz import f as pxyz
from hak.pf import f as pf

f = lambda table: (
  '|-'+'-|-'.join(['-'*len(f'{c}') for c in table['column_order']])+'-|'
)

def t_ac():
  x = {
    'table': insert_records(make_table(), [
      {'a': 0, 'c': 2},
      {'a': 3, 'c': 5},
      {'a': 6, 'c': 8}
    ])
  }
  y = '|---|---|'
  z = f(**x)
  return pxyz(x, y, z, new_line=1)

def t_abc():
  x = {
    'table': insert_records(make_table(), [
      {'a': 0, 'b': 1, 'c': 2},
      {'a': 3, 'b': 4, 'c': 5},
      {'a': 6, 'b': 7, 'c': 8}
    ])
  }
  y = '|---|---|---|'
  z = f(**x)
  return pxyz(x, y, z, new_line=1)

def t():
  if not t_ac(): return pf('!t_ac')
  if not t_abc(): return pf('!t_abc')
  return True
