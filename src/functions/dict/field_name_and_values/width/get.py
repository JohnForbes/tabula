from hak.pf import f as pf
from hak.pxyf import f as pxyf

# get_width
# f = lambda k, values: max(len(k), *[len(str(v)) for v in values])
f = lambda x: max(len(x['field_name']), *[len(str(v)) for v in x['values']])

t_field_name_dominant = lambda: pxyf(
  {'field_name': 'foo', 'values': [0, 1, 2, 3]},
  3,
  f
)

t_value_dominant = lambda: pxyf(
  {'field_name': 'foo', 'values': [0, 1000, 2000, 3000]},
  4,
  f
)

def t():
  if not t_field_name_dominant(): return pf('!t_field_name_dominant')
  if not t_value_dominant(): return pf('!t_value_dominant')
  return 1
