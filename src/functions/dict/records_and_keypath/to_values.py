from hak.pxyz import f as pxyz
from hak.pf import f as pf
from src.functions.dict.record_and_keypath.to_value import f as r_kp_to_val

# get_values
# f = lambda records, keypath: [_f(record, keypath) for record in records]
f = lambda x: [
  r_kp_to_val({'record': r, 'keypath': x['keypath']})
  for r
  in x['records']
]

def t_1():
  x = {
    'records': [{'a': 0}, {'a': 1}, {'a': 2}],
    'keypath': ('a', )
  }
  y = [0, 1, 2]
  z = f(x)
  return pxyz(x, y, z)

def t_2():
  x = {
    'records': [
      {'a': {'b': 0, 'c': 2}},
      {'a': {'b': 1, 'c': 1}},
      {'a': {'b': 2, 'c': 0}}
    ],
    'keypath': ('a', 'c')
  }
  y = [2, 1, 0]
  z = f(x)
  return pxyz(x, y, z)

def t_3():
  x = {
    'records': [
      {'a': {'b': {'d': 4, 'e': 7}, 'c': 2}},
      {'a': {'b': {'d': 5, 'e': 8}, 'c': 1}},
      {'a': {'b': {'d': 6, 'e': 9}, 'c': 0}}
    ],
    'keypath': ('a', 'b', 'd')
  }
  y = [4, 5, 6]
  z = f(x)
  return pxyz(x, y, z)

def t_4():
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
      }
    ],
    'keypath': ('Info', 'Appearance', 'Eye Colour')
  }
  y = ['Green', 'Brown', 'Blue']
  z = f(x)
  return pxyz(x, y, z)  

def t():
  if not t_1(): return pf('!t_1')
  if not t_2(): return pf('!t_2')
  if not t_3(): return pf('!t_3')
  if not t_4(): return pf('!t_4')
  return True
