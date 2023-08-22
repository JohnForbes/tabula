from hak.one.dict.rate.make import f as make_rate
from hak.pxyz import f as pxyz

from ...dict.records_and_index.to_padded_cell_values_of_col_width import f as g

f = lambda x: ['| '+' | '.join(g(x, r_i))+' |' for r_i in range(len(x))]

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
    '|    0.25 |     0.50 |     1.00 |      2.00 |       3.00 |   7.00 |',
    '|    0.75 |     1.00 |     4.00 |      5.00 |       6.00 |   7.00 |'
  ]
  z = f(x)
  return pxyz(x, y, z)
