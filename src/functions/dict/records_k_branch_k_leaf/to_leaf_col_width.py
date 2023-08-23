# ignore_overlength_lines
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from .to_col_width import f as records_k_branch_k_leaf_to_col_width
from data.records import records_without_date as _records

# get_col_w_fr_k_branch_k_leaf
# records_k_branch_k_leaf_to_leaf_col_width
f = lambda x: max(records_k_branch_k_leaf_to_col_width(x), len(x['k_branch']))

t_prices_apples = lambda: pxyf(
  {'records': _records, 'k_branch': 'prices', 'k_leaf': 'apples'},
  7,
  f
)

t_prices_bananas = lambda: pxyf(
  {'records': _records, 'k_branch': 'prices', 'k_leaf': 'bananas'},
  8,
  f
)

t_volumes_applezzz = lambda: pxyf(
  {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'applezzz'},
  8,
  f
)

t_volumes_bananazzz = lambda: pxyf(
  {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'bananazzz'},
  9,
  f
)

t_volumes_pearzzzzzz = lambda: pxyf(
  {'records': _records, 'k_branch': 'volumes', 'k_leaf': 'pearzzzzzz'},
  10,   
  f
)

t_zloops_zloop = lambda: pxyf(
  {'records': _records, 'k_branch': 'zloops', 'k_leaf': 'zloop'},
  6,
  f
)

def t():
  if not t_prices_apples(): return pf('!t_prices_apples')
  if not t_prices_bananas(): return pf('!t_prices_bananas')
  if not t_volumes_applezzz(): return pf('!t_volumes_applezzz')
  if not t_volumes_bananazzz(): return pf('!t_volumes_bananazzz')
  if not t_volumes_pearzzzzzz(): return pf('!t_volumes_pearzzzzzz')
  if not t_zloops_zloop(): return pf('!t_zloops_zloop')
  return 1
