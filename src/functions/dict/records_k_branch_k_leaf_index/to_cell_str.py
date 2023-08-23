# ignore_overlength_lines
from hak.one.dict.rate.to_str import f as rate_to_str
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ..records_k_branch_k_leaf.to_leaf_col_width import f as g
from data.records import records_without_date as _records

# f_x
# records_k_branch_k_leaf_index_to_cell_str
def f(x):
  record = x['records'][x['index']]
  rate = record[x['k_branch']][x['k_leaf']]
  return f"{rate_to_str(rate):>{g(x)}}"

def t_prices_apples_0():
  x = {
    'records': _records,
    'k_branch': 'prices',
    'k_leaf': 'apples',
    'index': 0
  }
  y = '   0.25'
  return pxyf(x, y, f)

def t_prices_bananas_0():
  x = {
    'records': _records,
    'k_branch': 'prices',
    'k_leaf': 'bananas',
    'index': 0
  }
  y = '    0.50'
  return pxyf(x, y, f)

def t_volumes_applezzz_0():
  x = {
    'records': _records,
    'k_branch': 'volumes',
    'k_leaf': 'applezzz',
    'index': 0
  }
  y = '    1.00'
  return pxyf(x, y, f)

def t_volumes_bananazzz_0():
  x = {
    'records': _records,
    'k_branch': 'volumes',
    'k_leaf': 'bananazzz',
    'index': 0
  }
  y = '     2.00'
  return pxyf(x, y, f)

def t_volumes_pearzzzzzz_0():
  x = {
    'records': _records,
    'k_branch': 'volumes',
    'k_leaf': 'pearzzzzzz',
    'index': 0
  }
  y = '      3.00'
  return pxyf(x, y, f)

def t_zloops_zloop_0():
  x = {
    'records': _records,
    'k_branch': 'zloops',
    'k_leaf': 'zloop',
    'index': 0
  }
  y = '  7.00'
  return pxyf(x, y, f)

def t_prices_apples_1():
  x = {
    'records': _records,
    'k_branch': 'prices',
    'k_leaf': 'apples',
    'index': 1
  }
  y = '   0.75'
  return pxyf(x, y, f)

def t_prices_bananas_1():
  x = {
    'records': _records,
    'k_branch': 'prices',
    'k_leaf': 'bananas',
    'index': 1
  }
  y = '    1.00'
  return pxyf(x, y, f)

def t_volumes_applezzz_1():
  x = {
    'records': _records,
    'k_branch': 'volumes',
    'k_leaf': 'applezzz',
    'index': 1
  }
  y = '    4.00'
  return pxyf(x, y, f)

def t_volumes_bananazzz_1():
  x = {
    'records': _records,
    'k_branch': 'volumes',
    'k_leaf': 'bananazzz',
    'index': 1
  }
  y = '     5.00'
  return pxyf(x, y, f)

def t_volumes_pearzzzzzz_1():
  x = {
    'records': _records,
    'k_branch': 'volumes',
    'k_leaf': 'pearzzzzzz',
    'index': 1
  }
  y = '      6.00'
  return pxyf(x, y, f)

def t_zloops_zloop_1():
  x = {
    'records': _records,
    'k_branch': 'zloops',
    'k_leaf': 'zloop',
    'index': 1
  }
  y = '  7.00'
  return pxyf(x, y, f)

def t():
  if not t_prices_apples_0():      return pf('!t_prices_apples_0')
  if not t_prices_bananas_0():     return pf('!t_prices_bananas_0')
  if not t_volumes_applezzz_0():   return pf('!t_volumes_applezzz_0')
  if not t_volumes_bananazzz_0():  return pf('!t_volumes_bananazzz_0')
  if not t_volumes_pearzzzzzz_0(): return pf('!t_volumes_pearzzzzzz_0')
  if not t_zloops_zloop_0():       return pf('!t_zloops_zloop_0')
  if not t_prices_apples_1():      return pf('!t_prices_apples_1')
  if not t_prices_bananas_1():     return pf('!t_prices_bananas_1')
  if not t_volumes_applezzz_1():   return pf('!t_volumes_applezzz_1')
  if not t_volumes_bananazzz_1():  return pf('!t_volumes_bananazzz_1')
  if not t_volumes_pearzzzzzz_1(): return pf('!t_volumes_pearzzzzzz_1')
  if not t_zloops_zloop_1():       return pf('!t_zloops_zloop_1')
  return 1
