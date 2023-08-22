# ignore_overlength_lines

from hak.one.dict.rate.make import f as make_rate
from hak.pf import f as pf
from hak.pxyz import f as pxyz

from ...strings.cell_strings.to_table_row import f as row_as_cells_to_row_as_str
from ..records_k_branch_k_leaf.to_k_branch_k_leaf_pairs import f as records_to_k_b_k_l_pairs
from ..records_k_branch_k_leaf.to_leaf_cell import f as records_k_branch_k_leaf_to_leaf_cell
from ..records_k_branch_k_leaf.to_unit_cell_str import f as records_k_branch_k_leaf_to_unit_cell_str

# f_t
# records_to_row_using_fn
def f(x):
  results = []
  pairs = records_to_k_b_k_l_pairs(x['records'])
  for (k_branch, k_leaf) in pairs:
    # print(f'k_branch: {k_branch}')
    # print(f'k_leaf: {k_leaf}')
    _result = x['function']({
      'records': x['records'],
      'k_branch': k_branch,
      'k_leaf': k_leaf
    })
    # print(f'_result: {_result}')
    results.append(_result)

  # print(f'results: {results}')
  
  final_result = row_as_cells_to_row_as_str(results, ' ')
  # print(f'final_result: {final_result}')
  # print()

  return final_result
  
  # return row_as_cells_to_row_as_str([
  #   x['function']({
  #     'records': x['records'],
  #     'k_branch': k_branch,
  #     'k_leaf': k_leaf
  #   })
  #   for (k_branch, k_leaf)
  #   in records_to_k_b_k_l_pairs(x['records'])
  # ])

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
  x = {
    'records': _records,
    'function': records_k_branch_k_leaf_to_leaf_cell
  }
  y  = '|  apples |  bananas | applezzz | bananazzz | pearzzzzzz |  zloop |'
  z = f(x)
  return pxyz(x, y, z)

def t_b():
  x = {
    'records': _records,
    'function': records_k_branch_k_leaf_to_unit_cell_str
  }
  y  = '| $/apple | $/banana |    apple |    banana |       pear |  zloop |'
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  return True
