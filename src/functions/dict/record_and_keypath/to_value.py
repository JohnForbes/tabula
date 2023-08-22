from hak.pf import f as pf
from hak.pxyz import f as pxyz

# f = lambda record, keypath: (
#   f(record[keypath[0]], keypath[1:])
#   if len(keypath) > 1 else
#   record[keypath[0]]
# )

f = lambda x: (
  f({
    'record': x['record'][x['keypath'][0]],
    'keypath': x['keypath'][1:]
  })
  if len(x['keypath']) > 1 else
  x['record'][x['keypath'][0]]
)

def t_a():
  x = {
    'record': {'a': {'b': 0, 'c': 2}},
    'keypath': ('a', 'c')
  }
  y = 2
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_a(): return pf('!t_a')
  return True
