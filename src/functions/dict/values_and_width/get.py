from hak.pxyz import f as pxyz

from src.functions.dict.value_and_width.to_str import f as make_line_value

# get_value_row_strings
f = lambda x: [
  make_line_value({'value': v, 'width': x['width']})
  for v
  in x['values']
]

def t():
  x = {
    'values': [0, 1, 2, 3],
    'width': 4
  }
  y = ['    0 ', '    1 ', '    2 ', '    3 ']
  z = f(x)
  return pxyz(x, y, z)
