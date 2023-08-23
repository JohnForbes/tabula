# ignore_overlength_lines
from datetime import date
from hak.one.dict.rate.make import f as make_rate
from hak.pf import f as pf
from hak.pxyf import f as pxyf

from data.records import records_without_date as _records

from ...dict.records_and_field_name.to_branch_col_width import f as f_a
from ...dict.records_and_function.to_sorted_keys_of_records import f as f_b
from ...strings.cell_strings.to_table_row import f as f_c

# records_to_top_border
f = lambda x: f_c({
  'cell_strings': ['-'*_ for _ in f_b({'records': x, 'function': f_a})],
  'char': '-'
})

t_nest = lambda: pxyf(
  _records,
  '|--------------------|-----------------------------------|--------|',
  f
)

def t_date():
  x = [
    {
      'date': date(2023, 7, 27),
      'prices': {'apples': make_rate(1, 4, {'$': 1, 'apple': -1})},
    },
    {
      'date': date(2023, 7, 28),
      'prices': {'apples': make_rate(3, 4, {'$': 1, 'apple': -1})},
    }
  ]
  y = "|------------|---------|"
  return pxyf(x, y, f)

def t():
  if not t_nest(): return pf('t_nest failed')
  # if not t_date(): return pf('t_date failed')
  return 1
