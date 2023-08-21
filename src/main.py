from hak.pf import f as pf
from hak.pxyz import f as pxyz
from src.block.make_from_flat_dict import f as make_block_from_flat_dict
from src.block.hstack import f as hstack

def f(x):
  _dicts = [[{k: x_i[k]} for x_i in x] for k in x[0].keys()]
  _blocks = [make_block_from_flat_dict(d) for d in _dicts]
  return '\n'.join(hstack(_blocks))

def t_a_b():
  n = 10
  x = [{'a': _, 'b': (n-1)-_} for _ in range(n)]
  y = '\n'.join([
    '---|---',
    ' a | b ',
    '---|---',
    *[f' {_} | {(n-1)-_} ' for _ in range(n)],
    '---|---'
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_a_b_c():
  n = 10
  x = [{'a': _, 'b': (n-1)-_, 'c': ((n-1)-_)*_} for _ in range(n)]
  y = '\n'.join([
    '---|---|----',
    ' a | b |  c ',
    '---|---|----',
    *[f' {_} | {(n-1)-_} | {((n-1)-_)*_:>2} ' for _ in range(n)],
    '---|---|----'
  ])
  z = f(x)
  return pxyz(x, [y], [z], new_line=1)

def t():
  if not t_a_b(): return pf('!t_a_b')
  if not t_a_b_c(): return pf('!t_a_b_c')
  return True
