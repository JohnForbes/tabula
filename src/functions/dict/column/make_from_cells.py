from hak.one.string.is_a import f as is_str
from hak.one.tuple.is_a import f as is_tuple
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.cell.is_a import f as is_cell
from src.functions.dict.cell.make import f as cell
from src.functions.dict.column.is_a import f as is_column

def f(x):
  name = x['name']
  cells = x['cells']
  path = None if 'path' not in x else x['path']
  for c in cells:
    if not is_cell(c):
      raise TypeError(f'cell, c: {c} was not of type cell')

  y = {'name': name, 'cells': cells}

  if path:
    if not any([is_tuple(path), is_str(path)]):
      raise NotImplementedError('Unexpected path type')

  y['path'] = (path if is_tuple(path) else tuple([path])) if path else tuple()
  return y

def t_a():
  _name = 'banana'
  x = {
    'name': _name,
    'path': None,
    'cells': [
      cell({'value': v, 'field_name': _name}) for v in ['b1', 'b2', 'b3']
    ]
  }
  z = f(x)
  if not is_column(z): return pf(f'not is_column(z); z: {z}')
  return 1

def t_d():
  _name = 'abc'
  x = {
    'name': _name,
    'cells': [cell({'value': v, 'field_name': _name}) for v in [0, 1, 2]]
  }
  y = {
    'name': 'abc',
    'cells': [cell({'value': v, 'field_name': 'abc'}) for v in [0, 1, 2]],
    'path': ()
  }
  return pxyf(x, y, f)

def t_path_as_str():
  x = {
    'name': 'abc',
    'path': 'root',
    'cells': [cell({'value': v, 'field_name': 'abc'}) for v in [0, 1, 2]]
  }
  y = {
    'name': 'abc',
    'cells': [cell({'value': v, 'field_name': 'abc'}) for v in [0, 1, 2]],
    'path': ('root',)
  }
  return pxyf(x, y, f)

def t_path():
  _name = 'abc'
  x = {
    'name': _name,
    'path': ('root', 'branch'),
    'cells': [cell({'value': v, 'field_name': _name}) for v in [0, 1, 2]]
  }
  y = {
    'name': 'abc',
    'cells': [cell({'value': v, 'field_name': 'abc'}) for v in [0, 1, 2]],
    'path': ('root', 'branch')
  }
  return pxyf(x, y, f)

def t():
  if not t_a(): return pf('!t_a')
  if not t_d(): return pf('!t_d')
  if not t_path(): return pf('!t_path')
  if not t_path_as_str(): return pf('!t_path_as_str')
  return 1
