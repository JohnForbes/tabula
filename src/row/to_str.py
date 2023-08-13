from hak.pxyz import f as pxyz
from src.cell.to_str import f as cell_to_str
from src.cell.make import f as make_cell

f = lambda x: '| '+' | '.join([cell_to_str(x[k]) for k in x])+' |'

def t():
  x = {'a': make_cell(1), 'b': make_cell(2), 'c': make_cell(3)}
  y = '| 1 | 2 | 3 |'
  z = f(x)
  return pxyz(x, y, z)
