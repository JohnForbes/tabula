from hak.many.dicts.a_into_b import f as a_into_b
from hak.one.dict.records_and_keypath.to_values import f as get_values
from hak.one.dict.value_and_width.to_str import f as make_line_value
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.record.get_leaf_keypaths import f as get_leaf_keypaths

from ...ints.cell_value_widths.to_aggregate_width import f as cell_W_to_row_w
from ..char_and_width.to_str import f as make_homogenous_line
from ..named_vector.width.get import f as get_width

records_leaf_paths_to_W = lambda x: [
  get_width({
    'name': keypath[-1],
    'values': get_values({'records': x['records'], 'keypath': keypath})
  })
  for keypath
  in x['leaf_paths']
]

# block.header.make
def f(x):
  leaf_paths = sorted(get_leaf_keypaths(x['records'][0], [], set()))
  leaf_paths = [_ for _ in leaf_paths if _[0] == x['keypath'][0]]
  leaf_Ws = records_leaf_paths_to_W(a_into_b({'leaf_paths': leaf_paths}, x))
  w = cell_W_to_row_w(leaf_Ws)
  return [
    make_homogenous_line({'char': '-', 'width': w}),
    make_line_value({'value': x['keypath'][-1], 'width': w})
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
