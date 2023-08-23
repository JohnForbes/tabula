from hak.pxyf import f as pxyf

from ...dict.records_and_index.to_padded_cell_values_of_col_width import f as fn
from data.records import records_without_date as _records

f = lambda x: [
  '| '+' | '.join(fn({'records': x, 'index': r_i}))+' |'
  for r_i
  in range(len(x))
]

# def f(x):
  # print(f'x: {x}')
  # print()
  # result = []
  # for r_i in range(len(x)):
  #   _ = fn({'records': x, 'index': r_i})
  #   result.append('| '+' | '.join(_)+' |')

  # return result

t = lambda: pxyf(
  _records,
  [
    '|    0.25 |     0.50 |     1.00 |      2.00 |       3.00 |   7.00 |',
    '|    0.75 |     1.00 |     4.00 |      5.00 |       6.00 |   7.00 |'
  ],
  f
)
