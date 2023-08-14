from src.table.insert_records import f as insert_records
from src.table.make import f as make_table
from hak.pxyz import f as pxyz
from hak.pf import f as pf

f = lambda table: (
  '|-'+'-|-'.join(['-'*len(f'{c}') for c in table['column_order']])+'-|'
)

# make_bar
# f = lambda x: "|-"+'-|-'.join(['-'*x['widths'][k] for k in x['names']])+"-|"

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

# def t_1():
#   x = {
#     'widths': {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6},
#     'names': list('abcde'),
#   }
#   y = '|----|-----|------|-------|--------|'
#   z = f(x)
#   return pxyz(x, y, z)

def t():
  if not t_ac(): return pf('!t_ac')
  if not t_abc(): return pf('!t_abc')
  # if not t_1(): return pf('!t_1')
  return True
