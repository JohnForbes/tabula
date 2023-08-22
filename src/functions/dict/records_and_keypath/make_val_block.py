from hak.pf import f as pf
from hak.pxyz import f as pxyz

# from misc.value_row_strings.get import f as get_value_row_strings
from src.functions.dict.values_and_width.get import f as get_value_row_strings

from src.functions.dict.char_and_width.to_str import f as make_homogenous_line
from src.functions.dict.field_name_and_values.width.get import f as get_width
from src.functions.dict.records_and_keypath.to_values import f as get_values
from src.functions.dict.value_and_width.to_str import f as make_line_value

# make_val_block
def f(x):
  keypath = x['keypath']
  k = keypath[-1]
  w = get_width({'field_name': k, 'values': get_values(x)})
  b = make_homogenous_line({'char': '-', 'width': w})
  return [
    make_line_value({'value': k, 'width': w}),
    b,
    *get_value_row_strings({'values': get_values(x), 'width': w}),
    b
  ]

def t_age():
  x = {
    'records': [
      {
        'Name': 'Alice',
        'Info': {
          'Age': 28,
          'Country': 'USA',
          'Appearance': {'Eye Colour': 'Green', 'Height': 1.85}
        }
      },
      {
        'Name': 'Bob',
        'Info': {
          'Age': 35,
          'Country': 'Canada',
          'Appearance': {'Eye Colour': 'Brown', 'Height': 1.79}
        }
      },
      {
        'Name': 'Charlie',
        'Info': {
          'Age': 22,
          'Country': 'UK',
          'Appearance': {'Eye Colour': 'Blue', 'Height': 1.62}
        }
      },
    ],
    'keypath': ('Info', 'Age')
  }
  y = [' Age ', '-----', '  28 ', '  35 ', '  22 ', '-----']
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_age(): return pf('!t_age')
  return True