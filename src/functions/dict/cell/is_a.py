from hak.one.bool.random.make import f as make_random_bool
from hak.one.dict.is_a import f as is_dict
from hak.one.list.random.make import f as make_random_list
from hak.one.number.float.random.make import f as make_random_float
from hak.one.number.int.random.make import f as make_random_int
from hak.one.set.random.make import f as make_random_set
from hak.one.string.random.make import f as make_random_str
from hak.one.tuple.random.make import f as make_random_tuple
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from .make import f as cell

def f(x):
  if not is_dict(x): return 0
  if len(x) != 3: return 0
  if 'value' not in x: return 0
  return 1

t_false_none               = lambda: pxyf(None, 0, f)
t_false_int                = lambda: pxyf(make_random_int(0, 10), 0, f)
t_false_float              = lambda: pxyf(make_random_float(), 0, f)
t_false_str                = lambda: pxyf(make_random_str(), 0, f)
t_false_set                = lambda: pxyf(make_random_set(), 0, f)
t_false_tuple              = lambda: pxyf(make_random_tuple(), 0, f)
t_false_bool               = lambda: pxyf(make_random_bool(), 0, f)
t_false_list               = lambda: pxyf(make_random_list(), 0, f)
t_false_dict_empty         = lambda: pxyf({}, 0, f)
t_false_dict_wrong_k_count = lambda: pxyf({'value': 0}, 0, f)
t_true                     = lambda: pxyf(cell({'value': 0, 'name': 'i'}), 1, f)

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
  return 1
