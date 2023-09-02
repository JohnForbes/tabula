from hak.pxyf import f as pxyf

from hak.one.dict.value_and_width.to_str import f as v_w_to_s

# get_value_row_strings
f = lambda x: [v_w_to_s({'value': v, 'width': x['width']}) for v in x['values']]

t = lambda: pxyf({'values': [0, 1, 2, 3], 'width': 4},
  ['    0 ', '    1 ', '    2 ', '    3 '],
  f
)
