from hak.pf import f as pf
from hak.one.dict.is_a import f as is_dict
from hak.one.list.is_a import f as is_list

# __init__
f = lambda columns=None, rows=None: {
  'columns': columns or [],
  'rows': rows or []
}

def t():
  z = f()
  if not is_dict(z): return pf('not is_dict(z)')
  if 'columns' not in z: return pf("'columns' not in z")
  if not is_list(z['columns']): return pf("not is_list(z['columns'])")
  if 'rows' not in z: return pf("'rows' not in z")
  if not is_list(z['rows']): return pf("not is_list(z['rows'])")
  return True
