# ignore_overlength_lines
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...dict.records_and_function.to_underlined_row import f as f_a
from ...dict.records_k_branch_k_leaf.to_leaf_cell import f as f_b
from data.records import records_without_date as _records

# records_to_sub_header_and_underline
f = lambda records: f_a({'records': records, 'function': f_b})

t_a = lambda: pxyf(
  _records,
  [
    '|  apples |  bananas | applezzz | bananazzz | pearzzzzzz |  zloop |',
    '|---------|----------|----------|-----------|------------|--------|'
  ],
  f
)

def t():
  if not t_a(): return pf('!t_a')
  return 1
