from hak.pf import f as pf
from hak.one.dict.is_a import f as is_dict
from hak.one.list.is_a import f as is_list

# __init__
f = lambda: {
  'column_names': [],
  'row_names': [],
  'cells': {}
}

def t():
  z = f()
  if not is_dict(z): return pf('not is_dict(z)')
  if 'column_names' not in z: return pf("'column_names' not in z")
  if not is_list(z['column_names']): return pf("not is_list(z['column_names'])")
  if 'row_names' not in z: return pf("'row_names' not in z")
  if not is_list(z['row_names']): return pf("not is_list(z['row_names'])")
  if 'cells' not in z: return pf("'cells' not in z")
  if not is_dict(z['cells']): return pf("not is_dict(z['cells'])")
  return True
