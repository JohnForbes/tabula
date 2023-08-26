# ignore_overlength_lines
from hak.pxyf import f as pxyf
from hak.one.dict.rate.make import f as make_rate

from ...dicts.records.to_first_record_sorted_keys import f as f_a
from ..records_and_name.to_sorted_leaf_keys import f as f_b

# f_n
# records_to_k_branch_k_leaf_pairs
# records_to_k_b_k_l_pairs
f = lambda x: [(a, b) for a in f_a(x) for b in f_b({'records': x, 'name': a})]

t = lambda: pxyf(
  [
    {
      'prices': {
        'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': make_rate(2, 4, {'$': 1, 'banana': -1})
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
        'bananas': make_rate(4, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': make_rate(4, 1, {'apple': 1}),
        'bananazzz': make_rate(5, 1, {'banana': 1}),
        'pearzzzzzz': make_rate(6, 1, {'pear': 1})
      },
      'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
    }
  ],
  [
    ('prices',  'apples'    ),
    ('prices',  'bananas'   ),
    ('volumes', 'applezzz'  ),
    ('volumes', 'bananazzz' ),
    ('volumes', 'pearzzzzzz'),
    ('zloops',  'zloop'     )
  ],
  f
)
