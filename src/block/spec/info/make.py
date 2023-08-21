from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.block.spec.info.header.make import f as make_info_header
from src.block.spec.info.not_header.make import f as make_info_not_header
from src.block.vstack import f as vstack

# make_b
def f(x, k):
  info_header = make_info_header(x, k)
  info_not_header = make_info_not_header(x, k)
  return vstack([
    info_header,
    info_not_header
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
    'k': ('Info',)
  }
  y = [
    '-------------------------------------',
    '                                Info ',
    '-------------------------------------',
    ' Age | Country |          Appearance ',
    '-----|---------|---------------------',
    '     |         | Eye Colour | Height ',
    '-----|---------|------------|--------',
    '  28 |     USA |      Green |   1.85 ',
    '  35 |  Canada |      Brown |   1.79 ',
    '  22 |      UK |       Blue |   1.62 ',
    '-----|---------|------------|--------'
  ]
  z = f(**x)
  return pxyz(x, y, z, new_line=1)

def t():
  if not t_a(): return pf('!t_a')
  return True
