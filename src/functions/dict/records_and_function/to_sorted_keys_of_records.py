# ignore_overlength_lines
from hak.one.dict.rate.make import f as rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf
from datetime import date

from ..records_and_name.to_branch_col_width import f as f_a
from ..records_and_name.to_pad_k_branch import f as f_b
from src.functions.dicts.records.to_first_record_sorted_keys import f as f_c
from data.records import records_without_date as _records

# records_and_fn_to_fn_applied_to_sorted_keys_of_records
f = lambda x: [
  x['function']({'records': x['records'], 'name': k}) for k
  in f_c(x['records'])
]

t_0 = lambda: pxyf({'records': _records, 'function': f_a}, [18, 33, 6], f)

t_1 = lambda: pxyf(
  {'records': _records, 'function': f_b},
  ['            prices', '                          volumes', 'zloops'],
  f
)

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
    'fn_a': f_a
  }
  y = ['      date', ' prices']
  return pxyf(x, y, f)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  # if not t_date(): return pf('!t_date')
  return 1
