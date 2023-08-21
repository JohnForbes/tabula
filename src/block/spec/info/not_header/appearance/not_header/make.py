from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.block.hstack import f as hstack
from .eye_col.make import f as make_eye_col_block
from .height.make import f as make_height_block

# make_appearance_not_header_block
# f = lambda x, k: hstack([
#   make_eye_col_block(x, ('Info', 'Appearance', 'Eye Colour')),
#   make_height_block(x, ('Info', 'Appearance', 'Height'))
# ])

def f(x, k):
  return hstack([
    make_eye_col_block(x, (*k, 'Eye Colour')),
    make_height_block(x, (*k, 'Height'))
  ])

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
    'k': ('Info', 'Appearance')
  }
  y = [
    ' Eye Colour | Height ',
    '------------|--------',
    '      Green |   1.85 ',
    '      Brown |   1.79 ',
    '       Blue |   1.62 ',
    '------------|--------'
  ]
  z = f(**x)
  return pxyz(x, y, z, new_line=1)

def t():
  if not t_a(): return pf('!t_a')
  return True
