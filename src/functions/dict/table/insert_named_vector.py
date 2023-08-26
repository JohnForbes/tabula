from hak.pxyf import f as pxyf
from ..cell.make import f as cell
from .make import f as table
from .make_row_identifier import f as make_row_identifier

def f(x):
  _name = x['named_vector']['name']

  _table = table()
  _table['column_order'] = x['table']['column_order'] + [_name]
  _table['row_order'] = x['table']['row_order']

  for v in x['named_vector']['values']:
    _ri = make_row_identifier(_table)
    _table['row_order'] = _table['row_order'] + [_ri]
    _table['cells'][(_name, _ri)] = cell({'value': v, 'name': _name})

  return _table

def t():
  x = {
    'table': table(),
    'named_vector': {
      'name': 'd',
      'values': [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    }
  }
  y = {
    'column_order': ['d'],
    'row_order': [_ for _ in range(10)],
    'cells': {('d', _): cell({'value': _/10, 'name': 'd'}) for _ in range(10)}
  }
  return pxyf(x, y, f)
