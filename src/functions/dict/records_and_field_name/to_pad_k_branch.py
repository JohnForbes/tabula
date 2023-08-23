# ignore_overlength_lines
from datetime import date
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from .to_sorted_leaf_keys import f as records_k_branch_to_sorted_leaf_keys
from ..records_k_branch_k_leaf.to_leaf_col_width import f as records_k_branch_k_leaf_to_leaf_col_width
from ...ints.cell_value_widths.to_aggregate_width import f as cell_val_widths_to_aggregate_width

# f_q
# records_to_pad_k_branch
def f(x):
  records = x['records']
  k_branch = x['field_name']
  j = records_k_branch_to_sorted_leaf_keys(x)
  q = [
    records_k_branch_k_leaf_to_leaf_col_width({
      'records': records,
      'k_branch': k_branch,
      'k_leaf': k
    }) for k in j
  ]
  w = abs(cell_val_widths_to_aggregate_width(q))
  return f'{k_branch:>{w}}'

from hak.one.dict.rate.make import f as make_rate
_records = [
  {
    'prices': {
      'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
      'bananas': make_rate(1, 2, {'$': 1, 'banana': -1})
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
      'bananas': make_rate(1, 1, {'$': 1, 'banana': -1})
    },
    'volumes': {
      'applezzz': make_rate(4, 1, {'apple': 1}),
      'bananazzz': make_rate(5, 1, {'banana': 1}),
      'pearzzzzzz': make_rate(6, 1, {'pear': 1})
    },
    'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
  }
]

t_prices = lambda: pxyf(
  {'records': _records, 'field_name': 'prices'},
  '            prices',
  f
)

t_volumes = lambda: pxyf(
  {'records': _records, 'field_name': 'volumes'},
  '                          volumes',
  f
)

t_zloops = lambda: pxyf(
  {'records': _records, 'field_name': 'zloops'},
  'zloops',
  f
)

def t_date():
  x = {
    'records': [
      {
        'date': date(2023, 7, 27),
        'prices': {
          'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
          'bananas': make_rate(1, 2, {'$': 1, 'banana': -1})
        },
        'volumes': {
          'applezzz': make_rate(1, 1, {'apple': 1}),
          'bananazzz': make_rate(2, 1, {'banana': 1}),
          'pearzzzzzz': make_rate(3, 1, {'pear': 1})
        },
        'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
      },
      {
        'date': date(2023, 7, 28),
        'prices': {
          'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
          'bananas': make_rate(1, 1, {'$': 1, 'banana': -1})
        },
        'volumes': {
          'applezzz': make_rate(4, 1, {'apple': 1}),
          'bananazzz': make_rate(5, 1, {'banana': 1}),
          'pearzzzzzz': make_rate(6, 1, {'pear': 1})
        },
        'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
      }
    ],
    'field_name': 'date'
  }
  return pxyf(x, 10, f)

def t():
  # if not t_date(): return pf('!t_date') # TODO
  if not t_prices(): return pf('!t_prices')
  if not t_volumes(): return pf('!t_volumes')
  if not t_zloops(): return pf('!t_zloops')
  return 1
