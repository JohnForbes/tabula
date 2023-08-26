from hak.one.string.is_a import f as is_str
from hak.one.tuple.is_a import f as is_tuple
from hak.pf import f as pf
from hak.pxyf import f as pxyf
from hak.one.dict.get_or_default import f as get_or_default

from src.functions.dict.column.is_a import f as is_column
from src.functions.dict.cell.make import f as cell
from src.functions.dict.name_and_values.to_cells import f as name_and_V_to_cells

def _validate(x):
  if x:
    if not any([is_tuple(x), is_str(x)]):
      raise NotImplementedError('Unexpected type')
  return x

_cast_to_tup = lambda x: (x if is_tuple(x) else tuple([x])) if x else tuple()

def f(x):
  y = {'name': x['name'], 'cells': name_and_V_to_cells(x)}
  y['path'] = _cast_to_tup(_validate(get_or_default(x, 'path', None)))
  return y

def t_a():
  x = {'name': 'banana', 'path': None, 'values': ['b1', 'b2', 'b3']}
  z = f(x)
  if not is_column(z): return pf(f'not is_column(z); z: {z}')
  return 1

def t_d():
  x = {'name': 'abc', 'values': [0, 1, 2]}
  y = {
    'name': 'abc',
    'cells': [cell({'value': v, 'name': 'abc'}) for v in [0, 1, 2]],
    'path': ()
  }
  return pxyf(x, y, f)

def t_path_as_str():
  x = {'name': 'abc', 'path': 'root', 'values': [0, 1, 2]}
  y = {
    'name': 'abc',
    'cells': [cell({'value': v, 'name': 'abc'}) for v in [0, 1, 2]],
    'path': ('root',)
  }
  return pxyf(x, y, f)

def t_path():
  x = {'name': 'abc', 'path': ('root', 'branch'), 'values': [0, 1, 2]}
  y = {
    'name': 'abc',
    'cells': [cell({'value': v, 'name': 'abc'}) for v in [0, 1, 2]],
    'path': ('root', 'branch')
  }
  return pxyf(x, y, f)

def t():
  if not t_a(): return pf('!t_a')
  if not t_d(): return pf('!t_d')
  if not t_path(): return pf('!t_path')
  if not t_path_as_str(): return pf('!t_path_as_str')
  return 1
