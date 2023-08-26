# ignore_overlength_lines
from datetime import date
from hak.one.dict.get_sorted_keys import f as get_sorted_keys
from hak.one.dict.rate.make import f as rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf

# records_k_branch_to_sorted_leaf_keys
f = lambda x: get_sorted_keys(x['records'][0][x['name']])

def t_prices():
  x = {
    'records': [
      {
        'prices': {
          'apples': rate(1, 4, {'$': 1, 'apple': -1}),
          'bananas': rate(1, 2, {'$': 1, 'banana': -1}),
        },
        '...': {}
      },
      {
        'prices': {
          'apples': rate(3, 4, {'$': 1, 'apple': -1}),
          'bananas': rate(1, 1, {'$': 1, 'banana': -1}),
        },
        '...': {}
      }
    ],
    'name': 'prices'
  }
  return pxyf(x, ['apples', 'bananas'], f)

def t_volumes():
  x = {
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
    'name': 'volumes'
  }
  return pxyf(x, ['applezzz', 'bananazzz', 'pearzzzzzz'], f)

def t_zloops():
  x = {
    'records': [
      {'...': {}, 'zloops': {'zloop': rate(7, 1, {'zloop': 1})}}, 
      {'...': {}, 'zloops': {'zloop': rate(7, 1, {'zloop': 1})}}
    ],
    'name': 'zloops'
  }
  return pxyf(x, ['zloop'], f)

def t_date():
  x = {
    'records': [
      {
        'date': date(2023, 7, 27),
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
        'date': date(2023, 7, 28),
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
    ],
    'name': 'date'
  }
  return pxyf(x, ['zloop'], f)

def t():
  if not t_prices(): return pf('!t_prices')
  if not t_volumes(): return pf('!t_volumes')
  if not t_zloops(): return pf('!t_zloops')
  # if not t_date(): return pf('!t_date')
  return 1
