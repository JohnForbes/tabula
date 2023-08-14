from hak.one.bool.random.make import f as make_random_bool
from hak.one.dict.is_a import f as is_dict
from hak.many.values.detect_type import f as detect_type
from hak.one.list.random.make import f as make_random_list
from hak.one.number.int.random.make import f as make_random_int
from hak.one.set.random.make import f as make_random_set
from hak.one.string.random.make import f as make_random_str
from hak.one.tuple.random.make import f as make_random_tuple
from hak.pf import f as pf
from hak.pxyz import f as pxyz
from hak.one.number.float.random.make import f as make_random_float
from src.cell.is_a import f as is_cell
from src.cell.make import f as make_cell

def f(x):
  if not is_dict(x): return False
  expected_keys = ['name', 'cells', 'path']
  for k in expected_keys:
    if k not in x:
      return False
  if len(x) != len(expected_keys): return False
  for c in x['cells']:
    if not is_cell(c):
      return False
  return True

def t_false_none():
  x = None
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_int():
  x = make_random_int(0, 10)
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_float():
  x = make_random_float()
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_str():
  x = make_random_str()
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_set():
  x = make_random_set()
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_tuple():
  x = make_random_tuple()
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_bool():
  x = make_random_bool()
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_list():
  x = make_random_list()
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_dict_empty():
  x = {}
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_dict_wrong_k_count():
  x = {'value': 0}
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_zero():
  x = 0
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_one():
  x = 1
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_dict():
  x = {'...': '...'}
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_extra_key():
  x = {'name': 'abc', 'cells': [0, 1, 2], 'extra': None}
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_false_cells_not_cells():
  x = {'name': 'carrot', 'cells': [0, 10, 100], 'path': None}
  y = False
  z = f(x)
  return pxyz(x, y, z)

def t_true():
  x = {'name': 'carrot', 'path': None}
  x['cells'] = [make_cell(v, x['name']) for v in [0, 10, 100]]
  y = True
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_false_bool(): return pf('!t_false_bool')
  if not t_false_dict_empty(): return pf('!t_false_dict_empty')
  if not t_false_dict_wrong_k_count(): return pf('!t_false_dict_wrong_k_count')
  if not t_false_dict(): return pf('!t_false_dict')
  if not t_false_extra_key(): return pf('!t_false_extra_key')
  if not t_false_float(): return pf('!t_false_float')
  if not t_false_int(): return pf('!t_false_int')
  if not t_false_list(): return pf('!t_false_list')
  if not t_false_none(): return pf('!t_false_none')
  if not t_false_one(): return pf('!t_false_one')
  if not t_false_set(): return pf('!t_false_set')
  if not t_false_str(): return pf('!t_false_str')
  if not t_false_tuple(): return pf('!t_false_tuple')
  if not t_false_zero(): return pf('!t_false_zero')
  if not t_false_cells_not_cells(): return pf('!t_false_cells_not_cells')
  if not t_true(): return pf('!t_true')
  return True
