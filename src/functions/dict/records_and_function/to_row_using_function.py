# ignore_overlength_lines

from hak.many.dicts.a_into_b import f as a_into_b
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from data.records import records_without_date as _records

from ...strings.cell_strings.to_table_row import f as f_a
from ..records_k_branch_k_leaf.to_k_branch_k_leaf_pairs import f as f_b
from ..records_k_branch_k_leaf.to_leaf_cell import f as f_c
from ..records_k_branch_k_leaf.to_unit_cell_str import f as f_d

# f_t
# records_to_row_using_fn
def f(x):
  results = [
    x['function'](a_into_b({'k_branch': k_branch, 'k_leaf': k_leaf}, x))
    for (k_branch, k_leaf) in f_b(x['records'])
  ]
  return f_a({'cell_strings': results, 'char': ' '})

t_a = lambda: pxyf(
  {'records': _records, 'function': f_c},
  '|  apples |  bananas | applezzz | bananazzz | pearzzzzzz |  zloop |',
  f
)

t_b = lambda: pxyf(
  {'records': _records, 'function': f_d},
  '| $/apple | $/banana |    apple |    banana |       pear |  zloop |',
  f
)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  return 1
