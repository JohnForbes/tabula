# ignore_overlength_lines

from hak.one.dict.rate.make import f as make_rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...strings.cell_strings.to_table_row import f as j
from ..records_k_branch_k_leaf.to_k_branch_k_leaf_pairs import f as get_pairs
from ..records_k_branch_k_leaf.to_leaf_cell import f as h
from ..records_k_branch_k_leaf.to_unit_cell_str import f as g

from hak.many.dicts.a_into_b import f as a_into_b

# f_t
# records_to_row_using_fn
def f(x):
  results = [
    x['function'](a_into_b({'k_branch': k_branch, 'k_leaf': k_leaf}, x))
    for (k_branch, k_leaf) in get_pairs(x['records'])
  ]
  return j({'cell_strings': results, 'col_separator_char': ' '})

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

def t_a():
  x = {'records': _records, 'function': h}
  y  = '|  apples |  bananas | applezzz | bananazzz | pearzzzzzz |  zloop |'
  return pxyf(x, y, f)

def t_b():
  x = {'records': _records, 'function': g}
  y  = '| $/apple | $/banana |    apple |    banana |       pear |  zloop |'
  return pxyf(x, y, f)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  return 1
