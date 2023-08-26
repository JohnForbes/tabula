from datetime import date
from hak.one.dict.rate.make import f as rate
from hak.one.dict.unit.to_str import f as unit_to_str
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...cell.make import f as cell
from ...cell.to_str import f as cell_to_str
from ..make_from_cells import f as column
from ..make_from_values import f as column_from_values

cell_to_unit_len_or_0 = lambda x: len(
  unit_to_str(x['value']['unit'])
  if x['type'] == 'rate' else
  ''
)

col_to_unit_len_or_0 = lambda x: cell_to_unit_len_or_0(x['cells'][0])

# width
f = lambda x: max(
  len(x['name']),
  *[len(cell_to_str(c)) for c in x['cells']],
  col_to_unit_len_or_0(x)
)

def t_apples():
  x = column({
    'name': 'apples',
    'cells': [cell({'value': _, 'name': 'apples'}) for _ in range(100)]
  })
  return pxyf(x, 6, f)

def t_cells_dominant_int():
  x = column({
    'name': 'a',
    'cells': [cell({'value': v, 'name': 'a'}) for v in [0, 1000, 2, 3]]
  })
  return pxyf(x, 4, f)

def t_name_dominant():
  x = column({
    'name': 'abc',
    'cells': [cell({'value': v, 'name': 'abc'}) for v in [0, 1, 2, 3]]
  })
  return pxyf(x, 3, f)

def t_cells_dominant_rate():
  x = column_from_values({
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
  x = column_from_values({
    'name':  'a',
    'values': [
      rate(0, 10, _unit),
      rate(1,  9, _unit),
      rate(2,  8, _unit),
      rate(3,  7, _unit)
    ]
  })
  return pxyf(x, len('$/banana'), f)

t_a = lambda: pxyf(
  {
    'name': 'a',
    'cells': [{'name': 'a', 'type': 'int', 'value': 0}],
    'path': ()
  },
  1,
  f
)

t_b = lambda: pxyf(
  {
    'name': 'abc',
    'cells': [
      {'name': 'abc', 'type': 'int', 'value': 0},
      {'name': 'abc', 'type': 'int', 'value': 10},
      {'name': 'abc', 'type': 'int', 'value': 23}
    ],
    'path': ()
  },
  3,
  f
)

t_c = lambda: pxyf(
  {
    'name': 'ab',
    'cells': [
      {'name': 'ab', 'type': 'int', 'value': 0},
      {'name': 'ab', 'type': 'int', 'value': 100},
      {'name': 'ab', 'type': 'int', 'value': 2300}
    ],
    'path': ()
  },
  4,
  f
)

t_d = lambda: pxyf(
  {
    'name': 'apples',
    'cells': [
      {'name': 'apples', 'type': 'int', 'value': 1},
      {'name': 'apples', 'type': 'int', 'value': 1},
      {'name': 'apples', 'type': 'int', 'value': 4},
      {'name': 'apples', 'type': 'int', 'value': 27},
      {'name': 'apples', 'type': 'int', 'value': 256},
      {'name': 'apples', 'type': 'int', 'value': 3125},
      {'name': 'apples', 'type': 'int', 'value': 46656},
      {'name': 'apples', 'type': 'int', 'value': 823543},
      {'name': 'apples', 'type': 'int', 'value': 16777216},
      {'name': 'apples', 'type': 'int', 'value': 387420489}
    ],
    'path': ()
  },
  9,
  f
)

t_e = lambda: pxyf(
  {
    'name': 'animal',
    'cells': [
      {'name': 'animal', 'type': 'str', 'value': 'dog'},
      {'name': 'animal', 'type': 'str', 'value': 'cat'},
      {'name': 'animal', 'type': 'str', 'value': 'fox'}
    ],
    'path': ()
  },
  6,
  f
)

t_f = lambda: pxyf(
  {
    'name': 'date',
    'cells': [
      {'name': 'date', 'type': 'date', 'value': date(2023, 1, 1)},
      {'name': 'date', 'type': 'date', 'value': date(2023, 4, 8)},
      {'name': 'date', 'type': 'date', 'value': date(2023, 12, 31)}
    ],
    'path': ()
  },
  10,
  f
)

t_g = lambda: pxyf(
  {
    'name': 'animal',
    'cells': [
      {'name': 'animal', 'type': 'str', 'value': 'dog'},
      {'name': 'animal', 'type': 'str', 'value': 'cat'},
      {'name': 'animal', 'type': 'str', 'value': 'fox'}
    ],
    'path': ()
  },
  6,
  f
)

t_h = lambda: pxyf(
  {
    'name': 'rate',
    'cells': [
      {
        'name': 'rate',
        'type': 'rate',
        'value': {'numerator': 0, 'denominator': 1, 'unit': {'m': 1}}
      },
      {
        'name': 'rate',
        'type': 'rate',
        'value': {'numerator': 1, 'denominator': 9, 'unit': {'m': 1}}
      },
      {
        'name': 'rate',
        'type': 'rate',
        'value': {'numerator': 1, 'denominator': 4, 'unit': {'m': 1}}
      }
    ],
    'path': ()
  },
  4,
  f
)

t_i = lambda: pxyf(
  {
    'name': 'rate',
    'cells': [
      {
        'name': 'rate',
        'type': 'rate',
        'value': {
          'numerator': 0,
          'denominator': 1,
          'unit': {'$': 1, 'banana': -1}
        }
      }, 
      {
        'name': 'rate',
        'type': 'rate',
        'value': {
          'numerator': 1,
          'denominator': 9,
          'unit': {'$': 1, 'banana': -1}
        }
      }, 
      {
        'name': 'rate',
        'type': 'rate',
        'value': {
          'numerator': 1,
          'denominator': 4,
          'unit': {'$': 1, 'banana': -1}
        }
      }
    ],
    'path': ()
  },
  8,
  f
)

def t():
  if not t_apples(): return pf('!t_a')
  if not t_name_dominant(): return pf('!t_name_dominant')
  if not t_cells_dominant_int(): return pf('!t_cells_dominant_int')
  if not t_cells_dominant_rate(): return pf('!t_cells_dominant_rate')
  if not t_long_unit(): return pf('!t_long_unit')

  if not t_a(): return pf('!t_a')
  if not t_b(): return pf('!t_b')
  if not t_c(): return pf('!t_c')
  if not t_d(): return pf('!t_d')
  if not t_e(): return pf('!t_e')
  if not t_f(): return pf('!t_f')
  if not t_g(): return pf('!t_g')
  if not t_h(): return pf('!t_h')
  if not t_i(): return pf('!t_i')

  return 1
