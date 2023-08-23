# ignore_overlength_lines
from hak.one.dict.rate.make import f as rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf
from datetime import date

from ..records_and_field_name.to_branch_col_width import f as get_top_head_width
from ..records_and_field_name.to_pad_k_branch import f as records_to_pad_k_branch
from src.functions.dicts.records.to_first_record_sorted_keys import f as get_K

# records_and_fn_to_fn_applied_to_sorted_keys_of_records
f = lambda x: [
  x['function']({'records': x['records'], 'field_name': k})
  for k
  in get_K(x['records'])
]

_records = [
  {
    'prices': {
      'apples': rate(1, 4, {'$': 1, 'apple': -1}),
      'bananas': rate(1, 2, {'$': 1, 'banana': -1})
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
      'bananas': rate(1, 1, {'$': 1, 'banana': -1})
    },
    'volumes': {
      'applezzz': rate(4, 1, {'apple': 1}),
      'bananazzz': rate(5, 1, {'banana': 1}),
      'pearzzzzzz': rate(6, 1, {'pear': 1})
    },
    'zloops': {'zloop': rate(7, 1, {'zloop': 1})}
  }
]

def t_0():
  x = {'records': _records, 'function': get_top_head_width}
  y = [18, 33, 6]
  return pxyf(x, y, f)

def t_1():
  x = {'records': _records, 'function': records_to_pad_k_branch}
  y = ['            prices', '                          volumes', 'zloops']
  return pxyf(x, y, f)

def t_date():
  x = {
    'records': [
      {
        'date': date(2023, 7, 27),
        'prices': {'apples': rate(1, 4, {'$': 1, 'apple': -1})}
      }, 
      {
        'date': date(2023, 7, 28),
        'prices': {'apples': rate(3, 4, {'$': 1, 'apple': -1})}
      }
    ],
    'fn_a': get_top_head_width
  }
  y = ['      date', ' prices']
  return pxyf(x, y, f)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  # if not t_date(): return pf('!t_date')
  return 1
