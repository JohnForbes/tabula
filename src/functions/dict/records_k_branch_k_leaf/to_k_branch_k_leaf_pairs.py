# ignore_overlength_lines
from hak.pxyf import f as pxyf
from hak.one.dict.rate.make import f as rate

from ...dicts.records.to_first_record_sorted_keys import f as f_a
from ..records_and_name.to_sorted_leaf_keys import f as f_b

from data.records import records_without_date as records_wout_date

# f_n
# records_to_k_branch_k_leaf_pairs
# records_to_k_b_k_l_pairs
f = lambda x: [(a, b) for a in f_a(x) for b in f_b({'records': x, 'name': a})]

t = lambda: pxyf(
  records_wout_date,
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
