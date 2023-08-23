# ignore_overlength_lines
from datetime import date
from hak.one.dict.get_sorted_keys import f as get_sorted_keys
from hak.one.dict.rate.make import f as make_rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf

# records_k_branch_to_sorted_leaf_keys
# f = lambda records, field_name: get_sorted_keys(records[0][field_name])
f = lambda x: get_sorted_keys(x['records'][0][x['field_name']])

def t_prices():
  x = {
    'records': [
      {
        'prices': {
          'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
          'bananas': make_rate(1, 2, {'$': 1, 'banana': -1}),
        },
        '...': {}
      },
      {
        'prices': {
          'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
          'bananas': make_rate(1, 1, {'$': 1, 'banana': -1}),
        },
        '...': {}
      }
    ],
    'field_name': 'prices'
  }
  return pxyf(x, ['apples', 'bananas'], f)

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
  return pxyf(x, ['applezzz', 'bananazzz', 'pearzzzzzz'], f)

def t_zloops():
  x = {
    'records': [
      {'...': {}, 'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}}, 
      {'...': {}, 'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}}
    ],
    'field_name': 'zloops'
  }
  return pxyf(x, ['zloop'], f)

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
  return pxyf(x, ['zloop'], f)

def t():
  if not t_prices(): return pf('!t_prices')
  if not t_volumes(): return pf('!t_volumes')
  if not t_zloops(): return pf('!t_zloops')
  # if not t_date(): return pf('!t_date')
  return 1
