from hak.pxyf import f as pxyf

from src.functions.dict.value_and_width.to_str import f as make_line_value

# get_value_row_strings
f = lambda x: [
  make_line_value({'value': v, 'width': x['width']})
  for v
  in x['values']
]

t = lambda: pxyf(
  {'values': [0, 1, 2, 3], 'width': 4},
  ['    0 ', '    1 ', '    2 ', '    3 '],
  f
)
