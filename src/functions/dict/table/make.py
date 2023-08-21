from hak.one.dict.is_a import f as is_dict
from hak.one.list.is_a import f as is_list
from hak.pf import f as pf

# __init__
f = lambda: {'column_order': [], 'row_order': [], 'cells': {}}

def t():
  z = f()
  if not is_dict(z): return pf('not is_dict(z)')
  if 'column_order' not in z: return pf("'column_order' not in z")
  if not is_list(z['column_order']): return pf("not is_list(z['column_order'])")
  if 'row_order' not in z: return pf("'row_order' not in z")
  if not is_list(z['row_order']): return pf("not is_list(z['row_order'])")
  if 'cells' not in z: return pf("'cells' not in z")
  if not is_dict(z['cells']): return pf("not is_dict(z['cells'])")
  return True
