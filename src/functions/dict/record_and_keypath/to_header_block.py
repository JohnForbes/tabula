from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.record.get_leaf_keypaths import f as get_leaf_keypaths
from src.functions.dict.value_and_width.to_str import f as make_line_value
from src.functions.dict.char_and_width.to_str import f as make_homogenous_line
from src.functions.dict.records_and_keypath.to_values import f as get_values
from src.functions.dict.field_name_and_values.width.get import f as get_width

# block.header.make
def f(x):
  records = x['records']
  keypath = x['keypath']
  leaf_paths = sorted(get_leaf_keypaths(records[0], [], set()))
  leaf_paths = [_ for _ in leaf_paths if _[0] == keypath[0]]
  
  _ = [
    get_width({
      'field_name': keypath[-1],
      'values': get_values({'records': records, 'keypath': keypath})
    })
    for keypath
    in leaf_paths
  ]

  w = sum(_) + 3*(len(_)-1)

  return [
    make_homogenous_line({'char': '-', 'width': w}),
    make_line_value({'value': keypath[-1], 'width': w})
  ]

def t_name():
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
    'keypath': ('Name', )
  }
  y = [
    '---------',
    '    Name ',
  ]
  return pxyf(x, y, f, new_line=1)

def t_info():
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
    'keypath': ('Info', )
  }
  y = [
    '-------------------------------------',
    '                                Info ',
  ]
  return pxyf(x, y, f, new_line=1)

def t():
  if not t_name(): return pf('!t_name')
  if not t_info(): return pf('!t_info')
  return True
