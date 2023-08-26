from hak.one.dict.rate.make import f as rate
from hak.one.dict.unit.to_str import f as unit_to_str
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...cell.make import f as cell
from ...cell.to_str import f as cell_to_str
from ..make_from_cells import f as make_column
from ..make_from_values import f as make_column_from_values

# width
def f(x):
  q = 0
  if x['cells'][0]['datatype'] == 'rate':
    q = len(unit_to_str(x['cells'][0]['value']['unit']))
  return max(len(x['name']), *[len(cell_to_str(c)) for c in x['cells']], q)

def t_a():
  x = make_column({
    'name': 'apples',
    'cells': [cell({'value': _, 'name': 'apples'}) for _ in range(100)]
  })
  return pxyf(x, 6, f)

def t_cells_dominant_int():
  x = make_column({
    'name': 'a',
    'cells': [cell({'value': v, 'name': 'a'}) for v in [0, 1000, 2, 3]]
  })
  return pxyf(x, 4, f)

def t_name_dominant():
  x = make_column({
    'name': 'abc',
    'cells': [cell({'value': v, 'name': 'abc'}) for v in [0, 1, 2, 3]]
  })
  return pxyf(x, 3, f)

def t_cells_dominant_rate():
  x = make_column_from_values({
    'name': 'a',
    'values': [
      rate(0, 10, {'m': 1}),
      rate(1,  9, {'m': 1}),
      rate(2,  8, {'m': 1}),
      rate(3,  7, {'m': 1})
    ]
  })
  return pxyf(x, 3, f)

def t_long_unit():
  _unit = {'$': 1, 'banana': -1}
  x = make_column_from_values({
    'name':  'a',
    'values': [
      rate(0, 10, _unit),
      rate(1,  9, _unit),
      rate(2,  8, _unit),
      rate(3,  7, _unit)
    ]
  })
  return pxyf(x, len('$/banana'), f)

def t():
  if not t_a(): return pf('!t_a')
  if not t_name_dominant(): return pf('!t_name_dominant')
  if not t_cells_dominant_int(): return pf('!t_cells_dominant_int')
  if not t_cells_dominant_rate(): return pf('!t_cells_dominant_rate')
  if not t_long_unit(): return pf('!t_long_unit')
  return 1
