from hak.one.string.find_last_char import f as find_last_char
from hak.pxyf import f as pxyf
from hak.pf import f as pf

# from hak.many.strings.lines._anon_0 import f as h
def _h(l, top_width):
  j = find_last_char(l, '|')+1
  d = l[0]*(top_width - len(l))
  return l[:j]+d+l[j:]

# h
f = lambda x: [_h(l, len(x[0])) for l in x]


def t_c():
  x = [
    '------------|---------',
    '    numbers | letters ',
    '-----|------|-----',
    ' abc |  ghi | jkl ',
    '-----|------|-----',
    '     |      |     ',
    '-----|------|-----',
    '     |      |   a ',
    '   1 |   10 |   b ',
    '   2 |  200 |   c ',
    '   3 | 3000 |   d ',
    '-----|------|-----'
  ]
  y = [
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
    '-----|------|---------'
  ]
  return pxyf(x, y, f)

def t():
  if not t_c(): return pf('!t_c')
  return 1
