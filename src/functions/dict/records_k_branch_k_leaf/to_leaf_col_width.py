# ignore_overlength_lines
from hak.one.dict.rate.make import f as make_rate
from hak.pf import f as pf
from hak.pxyz import f as pxyz

from .to_col_width import f as records_k_branch_k_leaf_to_col_width

# get_col_w_fr_k_branch_k_leaf
# records_k_branch_k_leaf_to_leaf_col_width
f = lambda x: max(records_k_branch_k_leaf_to_col_width(x), len(x['k_branch']))

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

def t_prices_apples():
  x = {'records': _records, 'k_branch': 'prices', 'k_leaf': 'apples'}
  y = 7
  z = f(x)
  return pxyz(x, y, z)

def t_prices_bananas():
  x = {'records': _records, 'k_branch': 'prices', 'k_leaf': 'bananas'}
  y = 8
  z = f(x)
  return pxyz(x, y, z)

def t_volumes_applezzz():
  x = {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'applezzz'}
  y = 8
  z = f(x)
  return pxyz(x, y, z)

def t_volumes_bananazzz():
  x = {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'bananazzz'}
  y = 9
  z = f(x)
  return pxyz(x, y, z)

def t_volumes_pearzzzzzz():
  x = {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'pearzzzzzz'}
  y = 10
  z = f(x)
  return pxyz(x, y, z)

def t_zloops_zloop():
  x = {'records': _records, 'k_branch': 'zloops', 'k_leaf': 'zloop'}
  y = 6
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_prices_apples(): return pf('!t_prices_apples')
  if not t_prices_bananas(): return pf('!t_prices_bananas')
  if not t_volumes_applezzz(): return pf('!t_volumes_applezzz')
  if not t_volumes_bananazzz(): return pf('!t_volumes_bananazzz')
  if not t_volumes_pearzzzzzz(): return pf('!t_volumes_pearzzzzzz')
  if not t_zloops_zloop(): return pf('!t_zloops_zloop')
  return True
