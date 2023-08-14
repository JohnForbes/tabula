from hak.many.values.detect_type import f as detect_type
from hak.one.string.is_a import f as is_str
from hak.one.tuple.is_a import f as is_tuple
from hak.pf import f as pf
from hak.pxyz import f as pxyz
from src.column.is_a import f as is_column
from src.cell.make import f as make_cell
from src.cell.is_a import f as is_cell

def f(name, cells, path=None):
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
  x = {'name': 'banana', 'path': None}
  x['cells'] = [make_cell(v, x['name']) for v in ['b1', 'b2', 'b3']]
  z = f(**x)
  if not is_column(z): return pf(f'not is_column(z); z: {z}')
  return True

def t_d():
  x = {'name': 'abc'}
  x['cells'] = [make_cell(v, x['name']) for v in [0, 1, 2]]
  y = {
    'name': 'abc',
    'cells': [make_cell(v, 'abc') for v in [0, 1, 2]],
    'path': ()
  }
  z = f(**x)
  return pxyz(x, y, z)

def t_path_as_str():
  x = {
    'name': 'abc',
    'path': 'root'
  }
  x['cells'] = [make_cell(v, 'abc') for v in [0, 1, 2]]
  y = {
    'name': 'abc',
    'cells': [make_cell(v, 'abc') for v in [0, 1, 2]],
    'path': ('root',)
  }
  z = f(**x)
  return pxyz(x, y, z)

def t_path():
  x = {
    'name': 'abc',
    'path': ('root', 'branch')
  }
  x['cells'] = [make_cell(v, x['name']) for v in [0, 1, 2]]
  y = {
    'name': 'abc',
    'cells': [make_cell(v, 'abc') for v in [0, 1, 2]],
    'path': ('root', 'branch')
  }
  z = f(**x)
  return pxyz(x, y, z)

def t():
  if not t_a(): return pf('!t_a')
  if not t_d(): return pf('!t_d')
  if not t_path(): return pf('!t_path')
  if not t_path_as_str(): return pf('!t_path_as_str')
  return True