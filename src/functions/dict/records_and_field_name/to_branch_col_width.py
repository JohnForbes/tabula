# ignore_overlength_lines
from hak.one.dict.rate.make import f as make_rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...ints.cell_value_widths.to_aggregate_width import f as cell_val_widths_to_aggregate_width
from ..records_k_branch_k_leaf.to_leaf_col_width import f as records_k_branch_k_leaf_to_leaf_col_width
from .to_sorted_leaf_keys import f as records_k_branch_to_sorted_leaf_keys

# dicts.records.k_branch.to_branch_col_width.py
# records_k_branch_to_branch_col_width

f = lambda x: cell_val_widths_to_aggregate_width([
  records_k_branch_k_leaf_to_leaf_col_width({
    'records': x['records'],
    'k_branch': x['field_name'],
    'k_leaf':  k
  })
  for k
  in records_k_branch_to_sorted_leaf_keys(x)
])

def t_prices():
  records = [
    {
      'prices': {
        'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(2, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': make_rate(1, 1, {'apple': 1}),
        'bananazzz': make_rate(2, 1, {'banana': 1}),
        'pearzzzzzz': make_rate(3, 1, {'pear': 1})
      },
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    },
    {
      'prices': {
        'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(4, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': make_rate(4, 1, {'apple': 1}),
        'bananazzz': make_rate(5, 1, {'banana': 1}),
        'pearzzzzzz': make_rate(6, 1, {'pear': 1})
      },
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    }
  ]
  x = {
    'records': records,
    'field_name': 'prices'
  }
  return pxyf(x, 18, f)

def t_volumes():
  x = {
    'records': [
      {
        '...': {},
        'volumes': {
          'applezzz': make_rate(1, 1, {'apple': 1}),
          'bananazzz': make_rate(2, 1, {'banana': 1}),
          'pearzzzzzz': make_rate(3, 1, {'pear': 1})
        },
        '...': {}
      }, 
      {
        '...': {},
        'volumes': {
          'applezzz': make_rate(4, 1, {'apple': 1}),
          'bananazzz': make_rate(5, 1, {'banana': 1}),
          'pearzzzzzz': make_rate(6, 1, {'pear': 1})
        },
        '...': {}
      }
    ],
    'field_name': 'volumes'
  }
  return pxyf(x, 33, f)

def t_zloops():
  x = {
    'records': [
      {
        '...': {},
        '...': {},
        'zloops': {
          'zloop': {'numerator': 7, 'denominator': 1, 'unit': {'zloop': 1}}
        }
      }, 
      {
        '...': {},
        '...': {},
        'zloops': {
          'zloop': {'numerator': 7, 'denominator': 1, 'unit': {'zloop': 1}}
        }
      }
    ],
    'field_name': 'zloops'
  }
  return pxyf(x, 6, f)

def t():
  if not t_prices(): return pf('!t_prices')
  if not t_volumes(): return pf('!t_volumes')
  if not t_zloops(): return pf('!t_zloops')
  return 1
