# ignore_overlength_lines
from hak.one.dict.rate.make import f as rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...ints.cell_value_widths.to_aggregate_width import f as f_a
from ..records_k_branch_k_leaf.to_leaf_col_width import f as f_b
from .to_sorted_leaf_keys import f as f_c

# dicts.records.k_branch.to_branch_col_width.py
# records_k_branch_to_branch_col_width
f = lambda x: f_a([
  f_b({'records': x['records'], 'k_branch': x['field_name'], 'k_leaf': k_leaf})
  for k_leaf
  in f_c(x)
])

t_prices = lambda: pxyf(
  {
    'records': [
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
    ],
    'field_name': 'prices'
  },
  18,
  f
)

t_volumes = lambda: pxyf(
  {
    'records': [
      {
        '...': {},
        'volumes': {
          'applezzz': rate(1, 1, {'apple': 1}),
          'bananazzz': rate(2, 1, {'banana': 1}),
          'pearzzzzzz': rate(3, 1, {'pear': 1})
        },
        '...': {}
      }, 
      {
        '...': {},
        'volumes': {
          'applezzz': rate(4, 1, {'apple': 1}),
          'bananazzz': rate(5, 1, {'banana': 1}),
          'pearzzzzzz': rate(6, 1, {'pear': 1})
        },
        '...': {}
      }
    ],
    'field_name': 'volumes'
  },
  33,
  f
)

t_zloops = lambda: pxyf(
  {
    'records': [
      {'...': {}, '...': {}, 'zloops': {'zloop': rate(7, 1, {'zloop': 1})}}, 
      {'...': {}, '...': {}, 'zloops': {'zloop': rate(7, 1, {'zloop': 1})}}
    ],
    'field_name': 'zloops'
  },
  6,
  f
)

def t():
  if not t_prices(): return pf('!t_prices')
  if not t_volumes(): return pf('!t_volumes')
  if not t_zloops(): return pf('!t_zloops')
  return 1
