from hak.pf import f as pf
from hak.pxyf import f as pxyf

# get_width
f = lambda x: max(len(x['name']), *[len(str(v)) for v in x['values']])

t_name_dominant = lambda: pxyf({'name': 'foo', 'values': [0, 1, 2, 3]}, 3, f)
t_value_dominant = lambda: pxyf({'name': 'foo', 'values': [0, 1000]}, 4, f)

def t():
  if not t_name_dominant(): return pf('!t_name_dominant')
  if not t_value_dominant(): return pf('!t_value_dominant')
  return 1
