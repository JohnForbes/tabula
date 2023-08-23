from datetime import date
from hak.one.list.remove_duplicates import f as remove_duplicates
from hak.one.string.find_last_char import f as find_last_char
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from ...column.make_from_values import f as column
from ...column.to_str import f as column_to_str
from ...column.width.get import f as get_column_width
from ....ints.cell_value_widths.to_aggregate_width import f as make_line_value

# from hak.many.strings.lines._anon_0 import f as h
def _h(l, top_width):
  j = find_last_char(l, '|')+1
  d = l[0]*(top_width - len(l))
  return l[:j]+d+l[j:]
h = lambda x: [_h(l, len(x[0])) if len(l) < len(x[0]) else l for l in x]

# from hak.cell_val_widths_to_aggregate_width import f as g
g = lambda x: sum(x)+(len(x)-1)*len(' | ')

def _f_a(columns, separator='|'):
  column_strings = [column_to_str(c) for c in columns]
  return '\n'.join([
    separator.join([
      column_strings[column_index].split('\n')[i]
      for column_index
      in range(len(columns))
    ])
    for i in range(len(column_strings[0].split('\n')))
  ])

_get_path_widths = lambda paths, columns: {
  p: max(
    make_line_value([
      get_column_width(c)
      for c
      in columns
      if c['path'][0] == p
    ]),
    len(p)
  )
  for p
  in paths
}

def _f_b(columns, separator='|'):
  paths = remove_duplicates(c['path'][0] for c in columns)
  path_widths = _get_path_widths(paths, columns)
  return '\n'.join(h([
    '-'+'-|-'.join([   '-'*path_widths[p]    for p in paths])+'-',
    ' '+' | '.join([f'{p:>{path_widths[p]}}' for p in paths])+' ',
    *_f_a(columns, separator).split('\n')
  ]))

f = lambda x='|': (
  _f_a if set([c['path'] for c in x['columns']]) == {()} else
  _f_b
)(x['columns'], x['separator'])

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
