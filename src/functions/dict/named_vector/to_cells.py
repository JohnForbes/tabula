from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ..cell.make import f as cell

f = lambda x: [cell({'name': x['name'], 'value': v}) for v in x['values']]

def t_a():
  _n = 'banana'
  _V = ['b1', 'b2', 'b3']
  return pxyf(
    {'name': _n, 'values': _V},
    [
      cell({'name': _n, 'value': _V[0]}),
      cell({'name': _n, 'value': _V[1]}),
      cell({'name': _n, 'value': _V[2]})
    ],
    f
  )

def t():
  if not t_a(): return pf('!t_a')
  return 1
