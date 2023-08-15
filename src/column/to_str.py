from datetime import date
from hak.one.dict.rate.make import f as make_rate
from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.cell.to_str import f as cell_to_str
from src.column.make_from_values import f as make_column
from src.column.width.get import f as get_width
from hak.one.dict.unit.to_str import f as unit_to_str

def f(x):
  _w = get_width(x)
  w = _w + 2
  cell_strings = [f" {cell_to_str(c):>{_w}} " for c in x['cells']]
  
  if x['cells'][0]['datatype'] == 'rate':
    return '\n'.join([
      '-'*w,
      f" {x['name']:>{_w}} ",
      '-'*w,
      f" {unit_to_str(x['cells'][0]['value']['unit']):>{_w}} ",
      '-'*w,
      *cell_strings,
      '-'*w,
    ])

  return '\n'.join([
    '-'*w,
    f" {x['name']:>{_w}} ",
    '-'*w,
    *cell_strings,
    '-'*w,
  ])

def t_0():
  x = make_column('a', [0])
  y = '\n'.join([
    '---',
    ' a ',
    '---',
    '   ',
    '---',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_1():
  x = make_column('abc', [0, 10, 23])
  y = '\n'.join([
    '-----',
    ' abc ',
    '-----',
    '     ',
    '  10 ',
    '  23 ',
    '-----',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_2():
  x = make_column('ab', [0, 100, 2300])
  y = '\n'.join([
    '------',
    '   ab ',
    '------',
    '      ',
    '  100 ',
    ' 2300 ',
    '------',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_3():
  x = make_column('apples', [_**_ for _ in range(10)])
  y = '\n'.join([
    '-----------',
    '    apples ',
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
  z = f(x)
  return pxyz(x, y, z, new_line=True)

def t_4():
  x = make_column('animal', ['dog', 'cat', 'fox'])
  y = '\n'.join([
    '--------',
    ' animal ',
    '--------',
    '    dog ',
    '    cat ',
    '    fox ',
    '--------',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=True)

def t_date():
  x = make_column(
    'date',
    [date(2023, 1, 1), date(2023, 4, 8), date(2023, 12, 31)]
  )
  y = '\n'.join([
    '------------',
    '       date ',
    '------------',
    ' 2023-01-01 ',
    ' 2023-04-08 ',
    ' 2023-12-31 ',
    '------------',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_str():
  x = make_column('animal', ['dog', 'cat', 'fox'])
  y = '\n'.join([
    '--------',
    ' animal ',
    '--------',
    '    dog ',
    '    cat ',
    '    fox ',
    '--------',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_rate():
  x = make_column(
    'rate',
    [
      make_rate(0, 10, {'m': 1}),
      make_rate(1,  9, {'m': 1}),
      make_rate(2,  8, {'m': 1})
    ]
  )
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
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_rate_long_unit():
  _unit = {'$': 1, 'banana': -1}
  x = make_column(
    'rate',
    [
      make_rate(0, 10, _unit),
      make_rate(1,  9, _unit),
      make_rate(2,  8, _unit)
    ]
  )
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
  z = f(x)
  return pxyz(x, y, z, new_line=1)

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
  return True
