from hak.pf import f as pf
from hak.pxyf import f as pxyf

from src.functions.dict.char_and_width.to_str import f as make_homogenous_line
from src.functions.dict.line.value.make import f as make_value_line

def f(x):
  if not x: return ''
  if len(x[0]) < 1: return ''
  k = list(x[0].keys())[0]
  values = [x_i[k] for x_i in x]
  w = max([len(str(k)), *[len(str(v)) for v in values]])
  b = make_homogenous_line({'char': '-', 'width': w})

  value_lines = [make_value_line({'value': v, 'width': w}) for v in values]

  row_strings = [
    b,
    make_value_line({'value': k, 'width': w}),
    b,
    *value_lines,
    b
  ]
  return row_strings

t_0 = lambda: pxyf([], '', f, new_line=1)
t_1 = lambda: pxyf([{}], '', f, new_line=1)

def t_a_0():
  x = [{'a': 0}]
  y = [
    '---',
    ' a ',
    '---',
    ' 0 ',
    '---'
  ]
  return pxyf(x, y, f, new_line=1)

def t_b_0():
  x = [{'b': 0}]
  y = [
    '---',
    ' b ',
    '---',
    ' 0 ',
    '---'
  ]
  return pxyf(x, y, f, new_line=1)

def t_a_10():
  x = [{'a': 10}]
  y = [
    '----',
    '  a ',
    '----',
    ' 10 ',
    '----'
  ]
  return pxyf(x, y, f, new_line=1)

def t_aaa_10():
  x = [{'aaa': 10}]
  y = [
    '-----',
    ' aaa ',
    '-----',
    '  10 ',
    '-----'
  ]
  return pxyf(x, y, f, new_line=1)

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
  return pxyf(x, y, f, new_line=1)

def t_a_0_to_9():
  x = [{'a': _} for _ in range(10)]
  y = [
    '---',
    ' a ',
    '---',
    *[f' {_} ' for _ in range(10)],
    '---'
  ]
  return pxyf(x, y, f, new_line=1)

def t():
  if not t_0(): return pf('!t_0')
  if not t_1(): return pf('!t_1')
  if not t_a_0(): return pf('!t_a_0')
  if not t_b_0(): return pf('!t_b_0')
  if not t_a_10(): return pf('!t_a_10')
  if not t_aaa_10(): return pf('!t_aaa_10')
  if not t_a_0_to_1(): return pf('!t_a_0_to_1')
  if not t_a_0_to_9(): return pf('!t_a_0_to_9')
  return 1
