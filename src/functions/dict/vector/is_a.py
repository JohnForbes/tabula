from hak.one.dict.is_a import f as is_dict
from hak.pf import f as pf
from hak.pxyf import f as pxyf

def f(x):
  if not is_dict(x): return False
  if 'name' not in x: return False
  if 'values' not in x: return False
  return True

t_a = lambda: pxyf({'a': '...', 'b': '...'}, 0, f)
t_b = lambda: pxyf({'name': 'foo', 'values': [0, 1, 2]}, 1, f)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  return 1
