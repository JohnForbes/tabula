from hak.one.dict.rate.to_str import f as rate_to_str
from hak.pf import f as pf
from hak.pxyf import f as pxyf
from hak.one.dict.rate.make import f as rate

# records_k_branch_k_leaf_to_leaf_values
f = lambda x: [rate_to_str(r[x['k_branch']][x['k_leaf']]) for r in x['records']]

from data.records import records_without_date as _records

def t_prices_apples():
  x = {'records': _records, 'k_branch': 'prices', 'k_leaf': 'apples'}
  y = ['0.25', '0.75']
  return pxyf(x, y, f)

def t_prices_bananas():
  x = {'records': _records, 'k_branch': 'prices', 'k_leaf': 'bananas'}
  y = ['0.50', '1.00']
  return pxyf(x, y, f)

def t_volumes_applezzz():
  x = {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'applezzz'}
  y = ['1.00', '4.00']
  return pxyf(x, y, f)

def t_volumes_bananazzz():
  x = {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'bananazzz'}
  y = ['2.00', '5.00']
  return pxyf(x, y, f)

def t_volumes_pearzzzzzz():
  x = {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'pearzzzzzz'}
  y = ['3.00', '6.00']
  return pxyf(x, y, f)

def t_zloops_zloop():
  x = {'records': _records, 'k_branch': 'zloops', 'k_leaf': 'zloop'}
  y = ['7.00', '7.00']
  return pxyf(x, y, f)

def t():
  if not t_prices_apples(): return pf('!t_prices_apples')
  if not t_prices_bananas(): return pf('!t_prices_bananas')
  if not t_volumes_applezzz(): return pf('!t_volumes_applezzz')
  if not t_volumes_bananazzz(): return pf('!t_volumes_bananazzz')
  if not t_volumes_pearzzzzzz(): return pf('!t_volumes_pearzzzzzz')
  if not t_zloops_zloop(): return pf('!t_zloops_zloop')
  return 1
