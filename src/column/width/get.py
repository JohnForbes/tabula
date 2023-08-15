from hak.pf import f as pf
from hak.pxyz import f as pxyz
from src.column.make_from_cells import f as make_column
from src.column.make_from_values import f as make_column_from_values
from src.cell.make import f as make_cell
from hak.one.dict.rate.make import f as make_rate
from src.cell.to_str import f as cell_to_str
from hak.one.dict.unit.to_str import f as unit_to_str

# width
def f(x):
  q = 0
  if x['cells'][0]['datatype'] == 'rate':
    q = len(unit_to_str(x['cells'][0]['value']['unit']))

  return max(
    len(x['name']),
    *[len(cell_to_str(c)) for c in x['cells']],
    q
  )

def t_a():
  x = make_column('apples', [make_cell(_, 'apples') for _ in range(100)])
  y = 6
  z = f(x)
  return pxyz(x, y, z)

def t_cells_dominant_int():
  x = make_column('a', [make_cell(v, 'a') for v in [0, 1000, 2, 3]])
  y = 4
  z = f(x)
  return pxyz(x, y, z)

def t_name_dominant():
  x = make_column('abc', [make_cell(v, 'abc') for v in [0, 1, 2, 3]])
  y = 3
  z = f(x)
  return pxyz(x, y, z)

def t_cells_dominant_rate():
  x = make_column_from_values(
    'a',
    [
      make_rate(0, 10, {'m': 1}),
      make_rate(1,  9, {'m': 1}),
      make_rate(2,  8, {'m': 1}),
      make_rate(3,  7, {'m': 1})
    ]
  )
  y = 3
  z = f(x)
  return pxyz(x, y, z)

def t_long_unit():
  _unit = {'$': 1, 'banana': -1}
  x = make_column_from_values(
    'a',
    [
      make_rate(0, 10, _unit),
      make_rate(1,  9, _unit),
      make_rate(2,  8, _unit),
      make_rate(3,  7, _unit)
    ]
  )
  y = len('$/banana')
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_a(): return pf('!t_a')
  if not t_name_dominant(): return pf('!t_name_dominant')
  if not t_cells_dominant_int(): return pf('!t_cells_dominant_int')
  if not t_cells_dominant_rate(): return pf('!t_cells_dominant_rate')
  if not t_long_unit(): return pf('!t_long_unit')
  return True
