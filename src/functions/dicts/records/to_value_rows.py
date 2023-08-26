from hak.pxyf import f as pxyf

from data.records import records_without_date as _records

from ...dict.records_and_index.to_padded_cell_values_of_col_width import f as g

f = lambda x: [
  '| '+' | '.join(g({'records': x, 'index': i}))+' |' for i in range(len(x))
]

t = lambda: pxyf(
  _records,
  [
    '|    0.25 |     0.50 |     1.00 |      2.00 |       3.00 |   7.00 |',
    '|    0.75 |     1.00 |     4.00 |      5.00 |       6.00 |   7.00 |'
  ],
  f
)
