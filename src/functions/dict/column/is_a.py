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

from src.functions.dict.cell.is_a import f as is_cell
from src.functions.dict.cell.make import f as cell

def f(x):
  if not is_dict(x): return 0
  expected_keys = ['name', 'cells', 'path']
  for k in expected_keys:
    if k not in x:
      return 0
  if len(x) != len(expected_keys): return 0
  for c in x['cells']:
    if not is_cell(c):
      return 0
  return 1

t_false_none = lambda: pxyf(None, 0, f)
t_false_int = lambda: pxyf(make_random_int(0, 10), 0, f)
t_false_float = lambda: pxyf(make_random_float(), 0, f)
t_false_str = lambda: pxyf(make_random_str(), 0, f)
t_false_set = lambda: pxyf(make_random_set(), 0, f)
t_false_tuple = lambda: pxyf(make_random_tuple(), 0, f)
t_false_bool = lambda: pxyf(make_random_bool(), 0, f)
t_false_list = lambda: pxyf(make_random_list(), 0, f)
t_false_dict_empty = lambda: pxyf({}, 0, f)
t_false_dict_wrong_k_count = lambda: pxyf({'value': 0}, 0, f)
t_false_zero = lambda: pxyf(0, 0, f)
t_false_one = lambda: pxyf(1, 0, f)
t_false_dict = lambda: pxyf({'...': '...'}, 0, f)

t_false_extra_key = lambda: pxyf(
  {'name': 'abc', 'cells': [0, 1, 2], 'extra': None},
  0,
  f
)

t_false_cells_not_cells = lambda: pxyf(
  {'name': 'carrot', 'cells': [0, 10, 100], 'path': None},
  0,
  f
)

def t_true_carrot():
  _name = 'carrot'
  x = {
    'name': _name,
    'path': None,
    'cells': [cell({'value': v, 'name': _name}) for v in [0, 10, 100]]
  }
  return pxyf(x, 1, f)

def t_true_banana():
  _name = 'banana'
  x = {
    'name': _name,
    'path': None,
    'cells': [cell({'value': v, 'name': _name}) for v in ['b1', 'b2', 'b3']]
  }
  return pxyf(x, 1, f)

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
  if not t_true_carrot(): return pf('!t_true_carrot')
  if not t_true_banana(): return pf('!t_true_banana')
  return 1
