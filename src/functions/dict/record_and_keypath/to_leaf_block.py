from hak.one.dict.get_max_depth import f as get_max_depth
from hak.one.dict.records_and_keypath.to_values import f as get_values
from hak.one.list.interleave import f as interleave
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...dict.char_and_width.to_str import f as make_homogenous_line
from ...dict.named_vector.width.get import f as get_width
from ...dict.value_and_width.to_str import f as make_line_value
from ...dict.values_and_width.get import f as get_value_row_strings

# block.leaf.make
def f(x):
  records = x['records']
  keypath = x['keypath']
  values = get_values(x)
  w = get_width({'name': keypath[-1], 'values': values})
  b = make_homogenous_line({'char': '-', 'width': w})
  q = [
    make_line_value({'value': keypath[-1], 'width': w}),
    *[
      make_homogenous_line({'char': ' ', 'width': w})
      for _
      in range(get_max_depth(records[0][keypath[0]], 0)-1)
    ]
  ]
  return [
    *interleave(q, b),
    b,
    *get_value_row_strings({'values': values, 'width': w}),
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
  y = [
    ' Age ',
    '-----',
    '     ',
    '-----',
    '  28 ',
    '  35 ',
    '  22 ',
    '-----'
  ]
  return pxyf(x, y, f, new_line=1)

def t_country():
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
    'keypath': ('Info', 'Country')
  }
  y = [
    ' Country ',
    '---------',
    '         ',
    '---------',
    '     USA ',
    '  Canada ',
    '      UK ',
    '---------'
  ]
  return pxyf(x, y, f, new_line=1)

def t():
  if not t_age(): return pf('!t_age')
  if not t_country(): return pf('!t_country')
  return True
