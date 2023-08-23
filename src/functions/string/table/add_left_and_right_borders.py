from hak.pxyf import f as pxyf

from src.functions.string.table.add_left_border import f as add_left
from src.functions.string.table.add_right_border import f as add_right

f = lambda x: add_right(add_left(x))

def t():
  x = '\n'.join([
    '---|---',
    ' a | b ',
    '---|---',
    ' 0 | 1 ',
    ' 3 | 4 ',
    ' 6 | 7 ',
    '---|---',
  ])
  y = '\n'.join([
    '|---|---|',
    '| a | b |',
    '|---|---|',
    '| 0 | 1 |',
    '| 3 | 4 |',
    '| 6 | 7 |',
    '|---|---|',
  ])
  return pxyf(x, y, f, new_line=1)
