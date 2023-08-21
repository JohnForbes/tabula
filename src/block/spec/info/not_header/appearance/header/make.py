from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.misc.dict.keypaths.leaf.get import f as get_leaf_keypaths
from src.misc.g import f as g
from src.misc.h import f as h
from src.misc.values.get import f as get_values
from src.misc.width.get import f as get_width

# make_j
# def f(x, k): return ["          Appearance "]

def f(x, k):
  leaf_paths = sorted(get_leaf_keypaths(x[0], [], set()))
  leaf_paths = [_ for _ in leaf_paths if len(_) > 1]
  leaf_paths = [_ for _ in leaf_paths if all([
    _[0] == k[0],
    _[1] == k[1]
  ])]

  # print(leaf_paths)

  _ = [
    get_width(keypath[-1], get_values(x, keypath))
    for keypath
    in leaf_paths
  ]

  # print(_)

  w = sum(_) + 3*(len(_)-1)

  return [
    # h('-', w),
    g(k[-1], w)
  ]

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
  y = ['          Appearance ',]
  z = f(**x)
  return pxyz(x, y, z, new_line=1)

def t():
  if not t_a(): return pf('!t_a')
  return True
