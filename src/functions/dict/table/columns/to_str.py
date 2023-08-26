from datetime import date
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ....dicts.columns.all_have_no_path import f as condition
from ....f_a import f as f_a
from ....f_b import f as f_b
from ...column.make_from_values import f as column

f = lambda x='|': (f_a if condition(x['columns']) else f_b)(x)

def t_00():
  x = {
    'columns': [
      column({'name': 'abc', 'values': [0, 1, 2, 3]}),
      column({'name': 'ghi', 'values': [0, 10, 200, 3000]})
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '-----|------',
    ' abc |  ghi ',
    '-----|------',
    '     |      ',
    '-----|------',
    '     |      ',
    '   1 |   10 ',
    '   2 |  200 ',
    '   3 | 3000 ',
    '-----|------',
  ])
  return pxyf(x, y, f, new_line=1)

def t_01():
  x = {
    'columns': [
      column({'name': 'abc', 'values': [0, 1, 2]}),
      column({'name': 'ghi', 'values': [0, 10, 2000]}),
      column({'name': 'jklm', 'values': ['abc', 'blergh', 'wragh']}),
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '-----|------|--------',
    ' abc |  ghi |   jklm ',
    '-----|------|--------',
    '     |      |        ',
    '-----|------|--------',
    '     |      |    abc ',
    '   1 |   10 | blergh ',
    '   2 | 2000 |  wragh ',
    '-----|------|--------',
  ])
  return pxyf(x, y, f, new_line=1)

def t_date():
  x = {
    'columns': [
      column({'name': 'abc', 'values': [0, 1, 2]}),
      column({'name': 'ghi', 'values': [0, 10, 2000]}),
      column({'name': 'jklm', 'values': ['abc', 'blergh', 'wragh']}),
      column({'name': 'date', 'values': [
        date(2023, m, 1)
        for m
        in range(1, 4)
      ]}),
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '-----|------|--------|------------',
    ' abc |  ghi |   jklm |       date ',
    '-----|------|--------|------------',
    '     |      |        |            ',
    '-----|------|--------|------------',
    '     |      |    abc | 2023-01-01 ',
    '   1 |   10 | blergh | 2023-02-01 ',
    '   2 | 2000 |  wragh | 2023-03-01 ',
    '-----|------|--------|------------',
  ])
  return pxyf(x, y, f, new_line=1)

def t_common_path():
  x = {
    'columns': [
      column({'name': 'abc', 'values': [0,  1,   2,    3], 'path': 'numbers'}),
      column({'name': 'ghi', 'values': [0, 10, 200, 3000], 'path': 'numbers'}),
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '------------',
    '    numbers ',
    '-----|------',
    ' abc |  ghi ',
    '-----|------',
    '     |      ',
    '-----|------',
    '     |      ',
    '   1 |   10 ',
    '   2 |  200 ',
    '   3 | 3000 ',
    '-----|------',
  ])
  return pxyf(x, y, f, new_line=1)

def t_numbers_let_paths():
  x = {
    'columns': [
      column({'name': 'abc', 'values': [0,  1,   2,    3], 'path': 'numbers'}),
      column({'name': 'ghi', 'values': [0, 10, 200, 3000], 'path': 'numbers'}),
      column({'name': 'jkl', 'values': list('abcd'), 'path': 'let'}),
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '------------|-----',
    '    numbers | let ',
    '-----|------|-----',
    ' abc |  ghi | jkl ',
    '-----|------|-----',
    '     |      |     ',
    '-----|------|-----',
    '     |      |   a ',
    '   1 |   10 |   b ',
    '   2 |  200 |   c ',
    '   3 | 3000 |   d ',
    '-----|------|-----',
  ])
  return pxyf(x, y, f, new_line=1)

def t_numbers_letters_paths():
  x = {
    'columns': [
      column({'name': 'abc', 'values': [0,  1,   2,    3], 'path': 'numbers'}),
      column({'name': 'ghi', 'values': [0, 10, 200, 3000], 'path': 'numbers'}),
      column({'name': 'jkl', 'values': list('abcd'), 'path': 'letters'}),
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '------------|---------',
    '    numbers | letters ',
    '-----|------|---------',
    ' abc |  ghi |     jkl ',
    '-----|------|---------',
    '     |      |         ',
    '-----|------|---------',
    '     |      |       a ',
    '   1 |   10 |       b ',
    '   2 |  200 |       c ',
    '   3 | 3000 |       d ',
    '-----|------|---------',
  ])
  return pxyf(x, y, f, new_line=1)

def t_numbers_letters_paths_2():
  x = {
    'columns': [
      column({'name': 'abc', 'values': [0,  1,   2,    3], 'path': 'numbers'}),
      column({'name': 'ghi', 'values': [0, 10, 200, 3000], 'path': 'numbers'}),
      column({'name': 'jkl', 'values': list('abcd'), 'path': 'letters'}),
      column({
        'name': 'mno',
        'values': ['a', 'bb', 'ccc', 'dddd'],
        'path': 'letters'
      }),
    ],
    'separator': '|'
  }
  y = '\n'.join([
    '------------|------------',
    '    numbers |    letters ',
    '-----|------|-----|------',
    ' abc |  ghi | jkl |  mno ',
    '-----|------|-----|------',
    '     |      |     |      ',
    '-----|------|-----|------',
    '     |      |   a |    a ',
    '   1 |   10 |   b |   bb ',
    '   2 |  200 |   c |  ccc ',
    '   3 | 3000 |   d | dddd ',
    '-----|------|-----|------',
  ])
  return pxyf(x, y, f, new_line=1)

def t():
  if not t_00(): return pf('!t_00')
  if not t_01(): return pf('!t_01')
  if not t_date(): return pf('!t_date')
  if not t_common_path(): return pf('!t_common_path')
  if not t_numbers_let_paths(): return pf('!t_numbers_let_paths')
  if not t_numbers_letters_paths(): return pf('!t_numbers_letters_paths')
  if not t_numbers_letters_paths_2(): return pf('!t_numbers_letters_paths_2')
  return 1
