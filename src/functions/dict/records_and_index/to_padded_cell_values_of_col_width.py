# ignore_overlength_lines
from hak.pf import f as pf
from hak.pxyf import f as pxyf
from hak.many.dicts.a_into_b import f as a_into_b

from ..records_k_branch_k_leaf_index.to_cell_str import f as fn_a
from ..records_k_branch_k_leaf.to_k_branch_k_leaf_pairs import f as fn_b
from data.records import records_without_date as _records

# f_y
# records_and_index_to_padded_cell_values_of_col_width
f = lambda x: [
  fn_a(a_into_b({'k_branch': k_b, 'k_leaf': k_l}, x))
  for (k_b, k_l)
  in fn_b(x['records'])
]

t_0 = lambda: pxyf(
  {'records': _records, 'index': 0},
  ['   0.25', '    0.50', '    1.00', '     2.00', '      3.00', '  7.00'],
  f
)

t_1 = lambda: pxyf(
  {'records': _records, 'index': 1},
  ['   0.75', '    1.00', '    4.00', '     5.00', '      6.00', '  7.00'],
  f
)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  return 1
