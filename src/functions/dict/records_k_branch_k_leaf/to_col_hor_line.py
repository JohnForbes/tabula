# ignore_overlength_lines
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from .to_leaf_col_width import f as f_b
from data.records import records_without_date as _records

# records_k_branch_k_leaf_to_col_hor_line
f = lambda x: '-'*f_b(x)

t_prices_apples = lambda: pxyf(
  {'records': _records, 'k_branch': 'prices', 'k_leaf': 'apples'},
  '-------',
  f
)

t_prices_bananas = lambda: pxyf(
  {'records': _records, 'k_branch': 'prices', 'k_leaf': 'bananas'},
  '--------',
  f
)

t_volumes_applezzz = lambda: pxyf(
  {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'applezzz'},
  '--------',
  f
)

t_volumes_bananazzz = lambda: pxyf(
  {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'bananazzz'},
  '---------',
  f
)

t_volumes_pearzzzzzz = lambda: pxyf(
  {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'pearzzzzzz'},
  '----------',
  f
)

t_zloops_zloop = lambda: pxyf(
  {'records': _records, 'k_branch': 'zloops', 'k_leaf': 'zloop'},
  '------',
  f
)

def t():
  if not t_prices_apples():      return pf('!t_prices_apples')
  if not t_prices_bananas():     return pf('!t_prices_bananas')
  if not t_volumes_applezzz():   return pf('!t_volumes_applezzz')
  if not t_volumes_bananazzz():  return pf('!t_volumes_bananazzz')
  if not t_volumes_pearzzzzzz(): return pf('!t_volumes_pearzzzzzz')
  if not t_zloops_zloop():       return pf('!t_zloops_zloop')
  return 1
