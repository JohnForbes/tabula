from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.cell.make import f as cell

f = lambda x: [cell({'name': x['name'], 'value': v}) for v in x['values']]

def t_a():
  _name = 'banana'
  _V = ['b1', 'b2', 'b3']
  x = {'name': _name, 'values': _V}
  y = [
    cell({'name': _name, 'value': _V[0]}),
    cell({'name': _name, 'value': _V[1]}),
    cell({'name': _name, 'value': _V[2]})
  ]
  return pxyf(x, y, f)

def t():
  if not t_a(): return pf('!t_a')
  return 1
