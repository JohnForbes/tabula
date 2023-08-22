from hak.pf import f as pf
from hak.pxyz import f as pxyz

# get_width
# f = lambda k, values: max(len(k), *[len(str(v)) for v in values])
f = lambda x: max(len(x['field_name']), *[len(str(v)) for v in x['values']])

def t_field_name_dominant():
  x = {'field_name': 'foo', 'values': [0, 1, 2, 3]}
  y = 3
  z = f(x)
  return pxyz(x, y, z)

def t_value_dominant():
  x = {'field_name': 'foo', 'values': [0, 1000, 2000, 3000]}
  y = 4
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_field_name_dominant(): return pf('!t_field_name_dominant')
  if not t_value_dominant(): return pf('!t_value_dominant')
  return True
