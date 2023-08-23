from hak.pxyf import f as pxyf

f = lambda x: '\n'.join([_x_i+'|' for _x_i in x.split('\n')])

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
    '---|---|',
    ' a | b |',
    '---|---|',
    ' 0 | 1 |',
    ' 3 | 4 |',
    ' 6 | 7 |',
    '---|---|',
  ])
  return pxyf(x, y, f, new_line=1)
