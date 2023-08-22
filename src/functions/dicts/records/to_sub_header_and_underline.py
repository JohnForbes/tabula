# ignore_overlength_lines
from hak.one.dict.rate.make import f as make_rate
from hak.pxyz import f as pxyz

from ...dict.records_and_function.to_underlined_row import f as records_and_fn_to_underlined_row
from ...dict.records_k_branch_k_leaf.to_leaf_cell import f as records_k_branch_k_leaf_to_leaf_cell

# records_to_sub_header_and_underline
f = lambda records: records_and_fn_to_underlined_row({
  'records': records,
  'function': records_k_branch_k_leaf_to_leaf_cell
})

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

def t():
  x = _records
  y = [
    '|  apples |  bananas | applezzz | bananazzz | pearzzzzzz |  zloop |',
    '|---------|----------|----------|-----------|------------|--------|'
  ]
  z = f(x)
  return pxyz(x, y, z)
