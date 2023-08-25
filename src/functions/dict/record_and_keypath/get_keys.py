from hak.pf import f as pf
from hak.pxyf import f as pxyf

# misc.dict.keys.get_keys_from_keypath
f = lambda x: (
  f({'dict': x['dict'][x['keypath'][0]], 'keypath': x['keypath'][1:]})
  if len(x['keypath']) > 1 else
  tuple(sorted(x['dict'][x['keypath'][0]].keys()))
)

def t_a():
  x = {
    'dict': {
      'Name': 'Alice',
      'Info': {
        'Age': 28,
        'Country': 'USA',
        'Appearance': {'Eye Colour': 'Green', 'Height': 1.85}
      }
    },
    'keypath': ('Info', 'Appearance')
  }
  y = ('Eye Colour', 'Height')
  return pxyf(x, y, f)

def t():
  if not t_a(): return pf('!t_a')
  return True
