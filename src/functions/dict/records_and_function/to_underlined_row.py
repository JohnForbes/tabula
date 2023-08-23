# ignore_overlength_lines

from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...dicts.records.to_horizontal_line import f as f_a
from ..records_and_function.to_row_using_function import f as f_b
from ..records_k_branch_k_leaf.to_leaf_cell import f as f_c
from ..records_k_branch_k_leaf.to_unit_cell_str import f as f_d
from data.records import records_without_date as _records

# records_and_fn_to_underlined_row
f = lambda x: [f_b(x), f_a(x['records'])]

t_leaf_keys = lambda: pxyf(
  {'records': _records, 'function': f_c},
  [
    '|  apples |  bananas | applezzz | bananazzz | pearzzzzzz |  zloop |',
    '|---------|----------|----------|-----------|------------|--------|'
  ],
  f
)

t_units = lambda: pxyf(
  {'records': _records, 'function': f_d},
  [
    '| $/apple | $/banana |    apple |    banana |       pear |  zloop |',
    '|---------|----------|----------|-----------|------------|--------|'
  ],
  f
)

def t():
  if not t_leaf_keys(): return pf('!t_leaf_keys')
  if not t_units(): return pf('!t_units')
  return 1
