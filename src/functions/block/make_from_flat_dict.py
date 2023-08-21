from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.functions.line.homogenous.make import f as make_homogenous_line
from src.functions.line.value.make import f as make_value_line

def f(x):
  if not x: return ''
  if len(x[0]) < 1: return ''
  k = list(x[0].keys())[0]
  values = [x_i[k] for x_i in x]
  w = max([len(str(k)), *[len(str(v)) for v in values]])
  b = make_homogenous_line('-', w)

  value_lines = [make_value_line(v, w) for v in values]

  row_strings = [
    b,
    make_value_line(k, w),
    b,
    *value_lines,
    b
  ]
  return row_strings

def t_0():
  x = []
  y = ''
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_1():
  x = [{}]
  y = ''
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_a_0():
  x = [{'a': 0}]
  y = [
    '---',
    ' a ',
    '---',
    ' 0 ',
    '---'
  ]
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_b_0():
  x = [{'b': 0}]
  y = [
    '---',
    ' b ',
    '---',
    ' 0 ',
    '---'
  ]
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_a_10():
  x = [{'a': 10}]
  y = [
    '----',
    '  a ',
    '----',
    ' 10 ',
    '----'
  ]
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_aaa_10():
  x = [{'aaa': 10}]
  y = [
    '-----',
    ' aaa ',
    '-----',
    '  10 ',
    '-----'
  ]
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_a_0_to_1():
  x = [{'a': 0}, {'a': 1}]
  y = [
    '---',
    ' a ',
    '---',
    ' 0 ',
    ' 1 ',
    '---'
  ]
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t_a_0_to_9():
  x = [{'a': _} for _ in range(10)]
  y = [
    '---',
    ' a ',
    '---',
    *[f' {_} ' for _ in range(10)],
    '---'
  ]
  z = f(x)
  return pxyz(x, y, z, new_line=1)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  if not t_a_0(): return pf('!t_a_0')
  if not t_b_0(): return pf('!t_b_0')
  if not t_a_10(): return pf('!t_a_10')
  if not t_aaa_10(): return pf('!t_aaa_10')
  if not t_a_0_to_1(): return pf('!t_a_0_to_1')
  if not t_a_0_to_9(): return pf('!t_a_0_to_9')
  return True