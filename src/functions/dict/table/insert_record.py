from hak.one.list.append_if_not_present import f as append_if_not_present
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ..cell.make import f as cell
from .make import f as table

def f(x):
  _table = x['table']
  _record = x['record']
  max_row_identifier = max(_table['row_order']) if _table['row_order'] else -1
  row_identifier = max_row_identifier+1
  _table['row_order'] = _table['row_order'] + [row_identifier]

  for (k, v) in _record.items():
    _table['column_order'] = append_if_not_present(_table['column_order'], k)
    _table['cells'][(k, row_identifier)] = cell({'value': v, 'name': k})

  return _table

def t_flat():
  x = {'table': table(), 'record': {'a': 0, 'b': 1, 'c': 2}}
  y = {
    'column_order': ['a', 'b', 'c'],
    'row_order': [0],
    'cells': {
      ('a', 0): cell({'value': 0, 'name': 'a'}),
      ('b', 0): cell({'value': 1, 'name': 'b'}),
      ('c', 0): cell({'value': 2, 'name': 'c'})
    }
  }
  return pxyf(x, y, f)

def t_nested():
  x = {'table': table(), 'record': {'prices': {'a': 0, 'b': 1, 'c': 2}}}
  y = {
    'column_order': ['a', 'b', 'c'],
    'row_order': [0],
    'cells': {
      ('a', 0): cell({'value': 0, 'name': 'a'}),
      ('b', 0): cell({'value': 1, 'name': 'b'}),
      ('c', 0): cell({'value': 2, 'name': 'c'})
    }
  }
  return pxyf(x, y, f)

def t():
  if not t_flat(): return pf('!t_flat')
  # if not t_nested(): return pf('!t_nested') # TODO
  return 1
