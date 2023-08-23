# ignore_overlength_lines
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...ints.cell_value_widths.to_aggregate_width import f as f_a
from ..records_k_branch_k_leaf.to_leaf_col_width import f as f_b
from .to_sorted_leaf_keys import f as f_c
from data.records import records_with_date
from data.records import records_without_date

# f_q
# records_to_pad_k_branch
def f(x):
  q = [
    f_b({
      'records': x['records'],
      'k_branch': x['field_name'],
      'k_leaf': k_leaf
    })
    for k_leaf
    in f_c(x)
  ]
  w = abs(f_a(q))
  return f"{x['field_name']:>{w}}"

t_prices = lambda: pxyf(
  {'records': records_without_date, 'field_name': 'prices'},
  '            prices',
  f
)

t_volumes = lambda: pxyf(
  {'records': records_without_date, 'field_name': 'volumes'},
  '                          volumes',
  f
)

t_zloops = lambda: pxyf(
  {'records': records_without_date, 'field_name': 'zloops'},
  'zloops',
  f
)

t_date = lambda: pxyf(
  {'records': records_with_date, 'field_name': 'date'},
  10,
  f
)

def t():
  # if not t_date(): return pf('!t_date') # TODO
  if not t_prices(): return pf('!t_prices')
  if not t_volumes(): return pf('!t_volumes')
  if not t_zloops(): return pf('!t_zloops')
  return 1
