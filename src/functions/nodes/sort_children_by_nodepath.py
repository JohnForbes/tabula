from hak.pxyz import f as pxyz

f = lambda s: sorted(s.children, key=lambda x: x.nodepath)

class N:
  def __init__(self, children=[], nodepath=''):
    self.children = children
    self.nodepath = nodepath
  
  __eq__ = lambda u, v: all([
    u.nodepath == v.nodepath,
    u.children == v.children
  ])

def t():
  x = N(children=[N([], 'xyz'), N([], 'uvw'), N([], 'mno'), N([], 'abc')])
  y = [
    N([], 'abc'),
    N([], 'mno'),
    N([], 'uvw'),
    N([], 'xyz'),
  ]
  z = f(x)
  return pxyz(x, y, z)
