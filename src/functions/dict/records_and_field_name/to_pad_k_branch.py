# ignore_overlength_lines
from datetime import date
from hak.pf import f as pf
from hak.pxyz import f as pxyz

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

def t_prices():
  x = {'records': _records, 'field_name': 'prices'}
  y = '            prices'
  z = f(x)
  return pxyz(x, y, z)

def t_volumes():
  x = {'records': _records, 'field_name': 'volumes'}
  y = '                          volumes'
  z = f(x)
  return pxyz(x, y, z)

def t_zloops():
  x = {'records': _records, 'field_name': 'zloops'}
  y = 'zloops'
  z = f(x)
  return pxyz(x, y, z)

def t_date():
  x = {
    'records': [
      {
        'date': date(2023, 7, 27),
        'prices': {
          'apples': {'numerator': 1, 'denominator': 4, 'unit': {'$': 1, 'apple': -1}},
          'bananas': {'numerator': 1, 'denominator': 2, 'unit': {'$': 1, 'banana': -1}}
        },
        'volumes': {
          'applezzz': {'numerator': 1, 'denominator': 1, 'unit': {'apple': 1}},
          'bananazzz': {'numerator': 2, 'denominator': 1, 'unit': {'banana': 1}},
          'pearzzzzzz': {'numerator': 3, 'denominator': 1, 'unit': {'pear': 1}}
        },
        'zloops': {'zloop': {'numerator': 7, 'denominator': 1, 'unit': {'zloop': 1}}}
      },
      {
        'date': date(2023, 7, 28),
        'prices': {
          'apples': {'numerator': 3, 'denominator': 4, 'unit': {'$': 1, 'apple': -1}},
          'bananas': {'numerator': 1, 'denominator': 1, 'unit': {'$': 1, 'banana': -1}}
        },
        'volumes': {
          'applezzz': {'numerator': 4, 'denominator': 1, 'unit': {'apple': 1}},
          'bananazzz': {'numerator': 5, 'denominator': 1, 'unit': {'banana': 1}},
          'pearzzzzzz': {'numerator': 6, 'denominator': 1, 'unit': {'pear': 1}}
        },
        'zloops': {'zloop': {'numerator': 7, 'denominator': 1, 'unit': {'zloop': 1}}}
      }
    ],
    'field_name': 'date'
  }
  y = 10
  z = f(x)
  return pxyz(x, y, z)

def t():
  # if not t_date(): return pf('!t_date')
  if not t_prices(): return pf('!t_prices')
  if not t_volumes(): return pf('!t_volumes')
  if not t_zloops(): return pf('!t_zloops')
  return True