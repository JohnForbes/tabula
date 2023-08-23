from hak.one.dict.is_a import f as is_dict
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from .strings.block.hstack import f as hstack
from .strings.block.make_from_flat_dict import f as make_block_from_flat_dict
from src.functions.dict.char_and_width.to_str import f as make_homogenous_line
from .dict.line.value.make import f as make_line_value

def f(x):
  if not any([is_dict(x[0][k]) for k in x[0]]):
    _leaf_dicts = [[{k: x_i[k]} for x_i in x] for k in x[0].keys()]
    _leaf_blocks = [make_block_from_flat_dict(d) for d in _leaf_dicts]
    return '\n'.join(hstack(_leaf_blocks))

  k_branch = 'a'
  _block_b_dicts = [x_i[k_branch] for x_i in x]
  _block_leaves = f(_block_b_dicts).split('\n')
  w = len(_block_leaves[0])-2
  
  _block_branch = [
    make_homogenous_line({'char': '-', 'width': w}),
    make_line_value({'value': k_branch, 'width': w})
  ]

  return '\n'.join([
    *_block_branch,
    *_block_leaves
  ])

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
  return pxyf(x, y, f, new_line=1)

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
  return pxyf(x, y, f, new_line=1)

def t_nested_a_aa_ab():
  x = [
    {'a': {'aa': 0, 'ab': 4}},
    {'a': {'aa': 1, 'ab': 3}},
    {'a': {'aa': 2, 'ab': 2}},
    {'a': {'aa': 3, 'ab': 1}},
    {'a': {'aa': 4, 'ab': 0}}
  ]
  y = '\n'.join([
    '---------',
    '       a ',
    '----|----',
    ' aa | ab ',
    '----|----',
    '  0 |  4 ',
    '  1 |  3 ',
    '  2 |  2 ',
    '  3 |  1 ',
    '  4 |  0 ',
    '----|----',
  ])
  return pxyf(x, y, f, new_line=1)

def t():
  if not t_a_b(): return pf('!t_a_b')
  if not t_a_b_c(): return pf('!t_a_b_c')
  if not t_nested_a_aa_ab(): return pf('!t_nested_a_aa_ab')
  return 1
