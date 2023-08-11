from hak.many.values.detect_type import f as detect_type
from hak.one.string.is_a import f as is_str
from hak.one.tuple.is_a import f as is_tup
from src.column.is_a import f as is_column
from hak.pf import f as pf

def f(name, values, datatype=None, path=None):
  y = {
    'name': name,
    'values': values,
    'datatype': datatype if datatype else detect_type(values)
  }

  if path:
    if not any([is_tup(path), is_str(path)]):
      raise NotImplementedError('Unexpected path type')

  y['path'] = (path if is_tup(path) else tuple([path])) if path else tuple()
  return y

def t():
  x = {'name': 'banana', 'values': ['b1', 'b2', 'b3']}
  z = f(**x)
  if not is_column(z): return pf(f'not is_column(z); z: {z}')
  return True
