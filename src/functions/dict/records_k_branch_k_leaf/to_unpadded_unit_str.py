from hak.one.dict.rate.make import f as make_rate
from hak.one.dict.unit.to_str import f as unit_to_str
from hak.pf import f as pf
from hak.pxyf import f as pxyf

# records_k_branch_k_leaf_to_unpadded_unit_str
f = lambda x: unit_to_str(x['records'][0][x['k_branch']][x['k_leaf']]['unit'])

def t_prices_apples():  
  x = {
    'records': [
      {
        'prices': {'apples': make_rate(1, 4, {'$': 1, 'apple': -1}), '...': {}},
        '...': {}
      },
      {}
    ],
    'k_branch': 'prices',
    'k_leaf': 'apples'
  }
  y = '$/apple'
  return pxyf(x, y, f)

def t_prices_bananas():  
  x = {
    'records': [
      {
        'prices': {
          '...': {},
          'bananas': make_rate(1, 2, {'$': 1, 'banana': -1})
        },
        '...': {}
      }, 
      {}
    ],
    'k_branch': 'prices',
    'k_leaf': 'bananas'
  }
  y = '$/banana'
  return pxyf(x, y, f)

def t_volumes_applezzz():  
  x = {
    'records': [
      {
        '...': {},
        'volumes': {'applezzz': make_rate(1, 1, {'apple': 1}), '...': {}},
      }, 
      {}
    ],
    'k_branch': 'volumes',
    'k_leaf': 'applezzz'
  }
  y = 'apple'
  return pxyf(x, y, f)

def t_volumes_bananazzz():  
  x = {
    'records': [
      {
        '...': {},
        'volumes': {'...': {}, 'bananazzz': make_rate(2, 1,{'banana': 1})}
      }, 
      {}
    ],
    'k_branch': 'volumes',
    'k_leaf': 'bananazzz'
  }
  y = 'banana'
  return pxyf(x, y, f)

def t_volumes_pearzzzzzz():  
  x = {
    'records': [
      {
        '...': {},
        'volumes': {'...': {}, 'pearzzzzzz': make_rate(3, 1, {'pear': 1})}
      }, 
      {}
    ],
    'k_branch': 'volumes',
    'k_leaf': 'pearzzzzzz'
  }
  y = 'pear'
  return pxyf(x, y, f)

def t_zloops_zloop():  
  x = {
    'records': [
      {
        '...': {},
        'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
      }, 
      {}
    ],
    'k_branch': 'zloops',
    'k_leaf': 'zloop'
  }
  y = 'zloop'
  return pxyf(x, y, f)

def t():
  if not t_prices_apples(): return pf('!t_prices_apples')
  if not t_prices_bananas(): return pf('!t_prices_bananas')
  if not t_volumes_applezzz(): return pf('!t_volumes_applezzz')
  if not t_volumes_bananazzz(): return pf('!t_volumes_bananazzz')
  if not t_volumes_pearzzzzzz(): return pf('!t_volumes_pearzzzzzz')
  if not t_zloops_zloop(): return pf('!t_zloops_zloop')
  return 1
