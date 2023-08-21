from hak.pf import f as pf
from hak.pxyz import f as pxyz

from .header.make import f as make_appearance_header_block
from .not_header.make import f as make_appearance_not_header_block
from src.block.vstack import f as vstack

def f(x, k):
  return vstack([
    make_appearance_header_block(x, k),
    make_appearance_not_header_block(x, k)
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
    '          Appearance ',
    '---------------------',
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
