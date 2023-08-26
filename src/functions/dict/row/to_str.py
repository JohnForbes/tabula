from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.cell.make import f as make_cell
from src.functions.dict.cell.to_str import f as cell_to_str

f = lambda x: '| '+' | '.join([cell_to_str(x[k]) for k in x])+' |'

def t_a():
  x = {
    'a': make_cell({'value': 1, 'name': 'a'}),
    'b': make_cell({'value': 2, 'name': 'b'}),
    'c': make_cell({'value': 3, 'name': 'c'})
  }
  y = '| 1 | 2 | 3 |'
  return pxyf(x, y, f)

def t():
  if not t_a(): return pf('!t_a')
  return 1
