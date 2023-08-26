# ignore_overlength_lines

from ...dict.records_k_branch_k_leaf.to_col_hor_line import f as f_a
from ...dict.records_k_branch_k_leaf.to_k_branch_k_leaf_pairs import f as f_b
from ...strings.cell_lines.to_row_line import f as f_c

from hak.one.dict.rate.make import f as rate
from hak.pxyf import f as pxyf

# records_to_horizontal_line
f = lambda x: f_c([
  f_a({'records': x, 'k_branch': a, 'k_leaf': b})
  for (a, b)
  in f_b(x)
])

def t():
  x = [
    {
      'prices': {
        'apples': rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': rate(2, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': rate(1, 1, {'apple': 1}),
        'bananazzz': rate(2, 1, {'banana': 1}),
        'pearzzzzzz': rate(3, 1, {'pear': 1})
      },
      'zloops': {'zloop': rate(7, 1, {'zloop': 1})}
    },
    {
      'prices': {
        'apples': rate(3, 4, {'$': 1, 'apple': -1}),
        'bananas': rate(4, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': rate(4, 1, {'apple': 1}),
        'bananazzz': rate(5, 1, {'banana': 1}),
        'pearzzzzzz': rate(6, 1, {'pear': 1})
      },
      'zloops': {'zloop': rate(7, 1, {'zloop': 1})}
    }
  ]
  y = '|---------|----------|----------|-----------|------------|--------|'
  return pxyf(x, y, f)
