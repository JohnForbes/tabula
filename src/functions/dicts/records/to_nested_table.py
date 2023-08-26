# ignore_overlength_lines
from datetime import date
from hak.one.dict.rate.make import f as rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from .to_horizontal_line import f as make_horizontal_line
from .to_k_branch_row import f as make_k_branch_row
from .to_sub_header_and_underline import f as make_subheader
from .to_top_border import f as make_top_border
from .to_units_row_with_underline import f as make_units_row
from .to_value_rows import f as make_value_rows

f = lambda x: '\n'.join([
  make_top_border(x),
  make_k_branch_row(x),
  make_horizontal_line(x),
  *make_subheader(x),
  *make_units_row(x),
  *make_value_rows(x),
  make_horizontal_line(x)
])

def t_nested():
  x = [
    {
      'prices': {
        'apples': rate(1, 4, {'$': 1, 'apple': -1}),
        'bananas': rate(2, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': rate(1, 1, {'apple': 1}),
        'bananazzz': rate(2, 1, {'banana': 1}),
        'pearzzzzzz': rate(3, 1, {'pear': 1})
      },
      'zloops': {'zloop': rate(7, 1, {'zloop': 1})}
    },
    {
      'prices': {
        'apples': rate(3, 4, {'$': 1, 'apple': -1}),
        'bananas': rate(4, 4, {'$': 1, 'banana': -1})
      },
      'volumes': {
        'applezzz': rate(4, 1, {'apple': 1}),
        'bananazzz': rate(5, 1, {'banana': 1}),
        'pearzzzzzz': rate(6, 1, {'pear': 1})
      },
      'zloops': {'zloop': rate(7, 1, {'zloop': 1})}
    }
  ]
  y = '\n'.join([
    "|--------------------|-----------------------------------|--------|",
    "|             prices |                           volumes | zloops |",
    "|---------|----------|----------|-----------|------------|--------|",
    "|  apples |  bananas | applezzz | bananazzz | pearzzzzzz |  zloop |",
    "|---------|----------|----------|-----------|------------|--------|",
    "| $/apple | $/banana |    apple |    banana |       pear |  zloop |",
    "|---------|----------|----------|-----------|------------|--------|",
    "|    0.25 |     0.50 |     1.00 |      2.00 |       3.00 |   7.00 |",
    "|    0.75 |     1.00 |     4.00 |      5.00 |       6.00 |   7.00 |",
    "|---------|----------|----------|-----------|------------|--------|",
  ])
  return pxyf(x, y, f, new_line=1)

def t_date():
  x = [
    {
      'dates': {'date': date(2023, 7, 27)},
      'prices': {'apples': rate(1, 4, {'$': 1, 'apple': -1})},
    },
    {
      'dates': {'date': date(2023, 7, 28)},
      'prices': {'apples': rate(3, 4, {'$': 1, 'apple': -1})},
    }
  ]
  y = '\n'.join([
    "|------------|---------|",
    "|      dates |  prices |",
    "|------------|---------|",
    "|       date |  apples |",
    "|------------|---------|",
    "|            | $/apple |",
    "|------------|---------|",
    "| 2023-07-27 |    0.25 |",
    "| 2023-07-28 |    0.75 |",
    "|------------|---------|",
  ])
  return pxyf(x, y, f, new_line=1)

def t():
  if not t_nested(): return pf('t_nested failed')
  # if not t_date(): return pf('t_date failed')
  return 1
