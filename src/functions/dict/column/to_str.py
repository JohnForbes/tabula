from datetime import date
from hak.one.dict.rate.make import f as rate
from hak.one.dict.unit.to_str import f as unit_to_str
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.cell.to_str import f as cell_to_str
from src.functions.dict.column.make_from_values import f as column
from src.functions.dict.column.width.get import f as get_width
from src.functions.dict.value_and_width.to_str import f as make_line_value
from src.functions.dict.char_and_width.to_str import f as make_homogenous_line

_f = lambda x: (
  unit_to_str(x['value']['unit']) if x['datatype'] == 'rate' else ''
)

def f(x):
  w = get_width(x)
  cell_strings = [f" {cell_to_str(c):>{w}} " for c in x['cells']]
  q = _f(x['cells'][0])
  return '\n'.join([
    make_homogenous_line({'char': '-', 'width': w}),
    make_line_value({'value': x['name'], 'width': w}),
    make_homogenous_line({'char': '-', 'width': w}),
    make_line_value({'value': q, 'width': w}),
    make_homogenous_line({'char': '-', 'width': w}),
    *cell_strings,
    make_homogenous_line({'char': '-', 'width': w}),
  ])

def t_0():
  x = column({'name': 'a', 'values': [0]})
  y = '\n'.join([
    '---',
    ' a ',
    '---',
    '   ',
    '---',
    '   ',
    '---',
  ])
  return pxyf(x, y, f, new_line=1)

def t_1():
  x = column({'name': 'abc', 'values': [0, 10, 23]})
  y = '\n'.join([
    '-----',
    ' abc ',
    '-----',
    '     ',
    '-----',
    '     ',
    '  10 ',
    '  23 ',
    '-----',
  ])
  return pxyf(x, y, f, new_line=1)

def t_2():
  x = column({'name': 'ab', 'values': [0, 100, 2300]})
  y = '\n'.join([
    '------',
    '   ab ',
    '------',
    '      ',
    '------',
    '      ',
    '  100 ',
    ' 2300 ',
    '------',
  ])
  return pxyf(x, y, f, new_line=1)

def t_3():
  x = column({'name': 'apples', 'values': [_**_ for _ in range(10)]})
  y = '\n'.join([
    '-----------',
    '    apples ',
    '-----------',
    '           ',
    '-----------',
    '         1 ',
    '         1 ',
    '         4 ',
    '        27 ',
    '       256 ',
    '      3125 ',
    '     46656 ',
    '    823543 ',
    '  16777216 ',
    ' 387420489 ',
    '-----------'
  ])
  return pxyf(x, y, f, new_line=True)

def t_4():
  x = column({'name': 'animal', 'values': ['dog', 'cat', 'fox']})
  y = '\n'.join([
    '--------',
    ' animal ',
    '--------',
    '        ',
    '--------',
    '    dog ',
    '    cat ',
    '    fox ',
    '--------',
  ])
  return pxyf(x, y, f, new_line=True)

def t_date():
  x = column({
    'name': 'date',
    'values': [date(2023, 1, 1), date(2023, 4, 8), date(2023, 12, 31)]
  })
  y = '\n'.join([
    '------------',
    '       date ',
    '------------',
    '            ',
    '------------',
    ' 2023-01-01 ',
    ' 2023-04-08 ',
    ' 2023-12-31 ',
    '------------',
  ])
  return pxyf(x, y, f, new_line=1)

def t_str():
  x = column({'name': 'animal', 'values': ['dog', 'cat', 'fox']})
  y = '\n'.join([
    '--------',
    ' animal ',
    '--------',
    '        ',
    '--------',
    '    dog ',
    '    cat ',
    '    fox ',
    '--------',
  ])
  return pxyf(x, y, f, new_line=1)

def t_rate():
  x = column({
    'name': 'rate',
    'values': [
      rate(0, 10, {'m': 1}),
      rate(1,  9, {'m': 1}),
      rate(2,  8, {'m': 1})
    ]
  })
  y = '\n'.join([
    '------',
    ' rate ',
    '------',
    '    m ',
    '------',
    '  0/1 ',
    '  1/9 ',
    '  1/4 ',
    '------',
  ])
  return pxyf(x, y, f, new_line=1)

def t_rate_long_unit():
  _unit = {'$': 1, 'banana': -1}
  x = column({
    'name':  'rate',
    'values': [
      rate(0, 10, _unit),
      rate(1,  9, _unit),
      rate(2,  8, _unit)
    ]
  })
  y = '\n'.join([
    '----------',
    '     rate ',
    '----------',
    ' $/banana ',
    '----------',
    '      0/1 ',
    '      1/9 ',
    '      1/4 ',
    '----------',
  ])
  return pxyf(x, y, f, new_line=1)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  if not t_2(): return pf('!t_2')
  if not t_3(): return pf('!t_3')
  if not t_4(): return pf('!t_4')
  if not t_date(): return pf('!t_date')
  if not t_str(): return pf('!t_str')
  if not t_rate(): return pf('!t_rate')
  if not t_rate_long_unit(): return pf('!t_rate_long_unit')
  return 1
