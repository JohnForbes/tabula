from hak.pxyz import f as pxyz

f = lambda x: '\n'.join(['|'+_x_i for _x_i in x.split('\n')])

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
    '|---|---',
    '| a | b ',
    '|---|---',
    '| 0 | 1 ',
    '| 3 | 4 ',
    '| 6 | 7 ',
    '|---|---',
  ])
  z = f(x)
  return pxyz(x, y, z, new_line=1)
