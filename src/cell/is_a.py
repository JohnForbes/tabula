from hak.one.bool.random.make import f as make_random_bool
from hak.one.dict.is_a import f as is_dict
from hak.one.get_datatype import f as detect_type
from hak.one.list.random.make import f as make_random_list
from hak.one.number.int.random.make import f as make_random_int
from hak.one.set.random.make import f as make_random_set
from hak.one.string.random.make import f as make_random_str
from hak.one.tuple.random.make import f as make_random_tuple
from hak.pf import f as pf
from hak.pxyz import f as pxyz
from hak.one.number.float.random.make import f as make_random_float

def f(x):
  if not is_dict(x): return False
  if len(x) != 2: return False
  if 'value' not in x: return False
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

def t_true():
  x = {'value': 0}
  x['datatype'] = detect_type(x['value'])
  y = True
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_false_bool(): return pf('!t_false_bool')
  if not t_false_none(): return pf('!t_false_none')
  if not t_false_int(): return pf('!t_false_int')
  if not t_false_float(): return pf('!t_false_float')
  if not t_false_str(): return pf('!t_false_str')
  if not t_false_set(): return pf('!t_false_set')
  if not t_false_tuple(): return pf('!t_false_tuple')
  if not t_false_list(): return pf('!t_false_list')
  if not t_false_dict_empty(): return pf('!t_false_dict_empty')
  if not t_false_dict_wrong_k_count(): return pf('!t_false_dict_wrong_k_count')
  if not t_true(): return pf('!t_true')
  return True
