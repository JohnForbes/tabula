from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.block.hstack import f as hstack
from .appearance.make import f as make_appearance_block
from src.block.leaf.make import f as make_leaf_block
from src.misc.dict.keypaths.leaf.get import f as get_leaf_keypaths

# make_info_not_header
def f(x, k):
  blocks = []
  leaf_keypaths = get_leaf_keypaths(x[0], keypaths=set(), path_so_far=[])
  for _k in x[0][k[0]]:
    _keypath = (k[0], _k)
    # print(_keypath, _keypath in leaf_keypaths)
    blocks.append(
      (
        make_leaf_block
        if _keypath in leaf_keypaths else
        make_appearance_block
      )(x, _keypath)
    )
  # age_block        = make_leaf_block(x, ('Info', 'Age'))
  # country_block    = make_leaf_block(x, ('Info', 'Country'))
  # appearance_block = make_appearance_block(x, ('Info', 'Appearance'))
  
  # print(f'age_block: {age_block}')
  # print(f'type(age_block): {type(age_block)}')
  
  # print(f'country_block: {country_block}')
  # print(f'type(country_block): {type(country_block)}')
  
  # print(f'appearance_block: {appearance_block}')
  # print(f'type(appearance_block): {type(appearance_block)}')
  # print()

  # return hstack([
  #   age_block,
  #   country_block,
  #   appearance_block
  # ])
  return hstack(blocks)

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
