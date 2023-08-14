from hak.many.values.detect_type import f as detect_type
from hak.one.string.is_a import f as is_str
from hak.one.tuple.is_a import f as is_tuple
from hak.pf import f as pf
from hak.pxyz import f as pxyz
from src.column.is_a import f as is_column

def f(name, values, path=None):
  y = {'name': name, 'values': values, 'datatype': detect_type(values)}

  if path:
    if not any([is_tuple(path), is_str(path)]):
      raise NotImplementedError('Unexpected path type')

  y['path'] = (path if is_tuple(path) else tuple([path])) if path else tuple()
  return y

def t_a():
  x = {'name': 'banana', 'values': ['b1', 'b2', 'b3']}
  z = f(**x)
  if not is_column(z): return pf(f'not is_column(z); z: {z}')
  return True

def t_b():
  x = {'name': 'abc', 'values': [0, 1, 2], 'path': ('root', 'branch')}
  y = {
    'name': 'abc',
    'values': [0, 1, 2],
    'datatype': 'int',
    'path': ('root', 'branch')
  }
  z = f(**x)
  return pxyz(x, y, z)

def t_c():
  x = {'name': 'abc', 'values': [0, 1, 2], 'path': 'root'}
  y = {
    'name': 'abc',
    'values': [0, 1, 2],
    'datatype': 'int',
    'path': ('root',)
  }
  z = f(**x)
  return pxyz(x, y, z)

def t_d():
  x = {'name': 'abc', 'values': [0, 1, 2]}
  y = {'name': 'abc', 'values': [0, 1, 2], 'datatype': 'int', 'path': ()}
  z = f(**x)
  return pxyz(x, y, z)

def t_0():
  x = {'name': 'abc', 'values': [0, 1, 2]}
  y = {'name': 'abc', 'values': [0, 1, 2], 'datatype': 'int', 'path': ()}
  z = f(**x)
  return pxyz(x, y, z)

def t_path_as_str():
  x = {'name': 'abc', 'values': [0, 1, 2], 'path': 'root'}
  y = {
    'name': 'abc',
    'values': [0, 1, 2],
    'datatype': 'int',
    'path': ('root',)
  }
  z = f(**x)
  return pxyz(x, y, z)

def t_path():
  x = {'name': 'abc', 'values': [0, 1, 2], 'path': ('root', 'branch')}
  y = {
    'name': 'abc',
    'values': [0, 1, 2],
    'datatype': 'int',
    'path': ('root', 'branch')
  }
  z = f(**x)
  return pxyz(x, y, z)

def t():
  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  if not t_c(): return pf('!t_c')
  if not t_d(): return pf('!t_d')
  if not t_0(): return pf('!t_0')
  if not t_path(): return pf('!t_path')
  if not t_path_as_str(): return pf('!t_path_as_str')
  return True
