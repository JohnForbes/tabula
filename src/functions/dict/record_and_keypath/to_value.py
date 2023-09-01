from hak.pf import f as pf
from hak.pxyf import f as pxyf

def f(x):
  if len(x['keypath']) > 1:
    _kp_0 = x['keypath'][0]
    _record = x['record']
    _kp_0_record = _record[_kp_0]
    _keypath = x['keypath'][1:]
    _x = {'record': _kp_0_record, 'keypath': _keypath}
    result = f(_x)
  else:
    result = x['record'][x['keypath'][0]]

  return result

# f = lambda x: (
#   f({
#     'record': x['record'][x['keypath'][0]],
#     'keypath': x['keypath'][1:]
#   })
#   if len(x['keypath']) > 1 else
#   x['record'][x['keypath'][0]]
# )

t_a = lambda: pxyf(
  {'record': {'a': {'b': 0, 'c': 2}}, 'keypath': ('a', 'c')},
  2,
  f
)

def t():
  if not t_a(): return pf('!t_a')
  return 1
