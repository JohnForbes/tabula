from hak.one.dict.rate.make import f as rate
from hak.one.dict.rate.to_num import f as to_num
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ....dict.cell.make import f as cell
from ....dict.cell.width.get import f as get_w

f = lambda x: {
  k: max([
    get_w(cell({'value': r[k] if k in r else None, 'name': k}))
    for r in x['records']
  ])
  for k in x['names']
}

def t_a():
  x = {
    'names': list('abcde'),
    'records': [
      {'a':  0, 'b':  1, 'c':  2, 'd':  3, 'e':  4},
      {'a':  5, 'b':  6, 'c':  7, 'd':  8, 'e':  9},
      {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14},
    ]
  }
  y = {k: 2 for k in list('abcde')}
  return pxyf(x, y, f)

def t_b():
  x = {
    'names': list('abcde'),
    'records': [
      {'a':  0, 'b':  1, 'c':  2, 'd': to_num(rate( 3, 1, {'m': 1})), 'e':  4},
      {'a':  5, 'b':  6, 'c':  7, 'd': to_num(rate( 8, 1, {'m': 1})), 'e':  9},
      {'a': 10, 'b': 11, 'c': 12, 'd': to_num(rate(13, 1, {'m': 1})), 'e': 14},
    ]
  }
  y = {k: 2 for k in list('abcde')}
  return pxyf(x, y, f)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  return True
