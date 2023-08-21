from hak.one.dict.get_max_depth import f as get_max_depth
from hak.one.list.interleave import f as interleave
from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.misc.g import f as g
from src.misc.h import f as h
from src.misc.value_row_strings.get import f as get_value_row_strings
from src.misc.values.get import f as get_values
from src.misc.width.get import f as get_width

def f(x, k):
  values = get_values(x, k)
  w = get_width(k[-1], values)
  b = h('-', w)
  q = [g(k[-1], w), *[h(' ', w) for _ in range(get_max_depth(x[0][k[0]], 0)-2)]]
  return [*interleave(q, b), b, *get_value_row_strings(values, w), b]

def t_a():
  x = {
    'x': [
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
    'k': ('Info', 'Appearance', 'Height')
  }
  y = [
    ' Height ',
    '--------',
    '   1.85 ',
    '   1.79 ',
    '   1.62 ',
    '--------'
  ]
  z = f(**x)
  return pxyz(x, y, z, new_line=1)

def t():
  if not t_a(): return pf('!t_a')
  return True
