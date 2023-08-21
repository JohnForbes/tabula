from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.functions.dict.cell.make import f as make_cell
from src.functions.dict.cell.to_str import f as cell_to_str

f = lambda x: '| '+' | '.join([cell_to_str(x[k]) for k in x])+' |'

def t_0():
  x = {'a': make_cell(1, 'a'), 'b': make_cell(2, 'b'), 'c': make_cell(3, 'c')}
  y = '| 1 | 2 | 3 |'
  z = f(x)
  return pxyz(x, y, z)

# def t_a():
#   x = ['   0.25', '    0.50', '    1.00', '     2.00', '      3.00', '  7.00']
#   y = '|    0.25 |     0.50 |     1.00 |      2.00 |       3.00 |   7.00 |'
#   z = f(x)
#   return pxyz(x, y, z)

# def t_b():
#   x = ['   0.75', '    1.00', '    4.00', '     5.00', '      6.00', '  7.00']
#   y = '|    0.75 |     1.00 |     4.00 |      5.00 |       6.00 |   7.00 |'
#   z = f(x)
#   return pxyz(x, y, z)

def t():
  if not t_0(): return pf('!t_0')
  # if not t_a(): return pf('!t_a')
  # if not t_b(): return pf('!t_b')
  return True
