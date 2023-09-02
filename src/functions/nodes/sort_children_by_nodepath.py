from hak.pxyz import f as pxyz

f = lambda s: sorted(s.children, key=lambda x: x.nodepath)

def t():
  from importlib import import_module
  N = import_module('src.classes.node').Node
  T = import_module('src.classes.table').Table
  _t = T()
  _n = N('root', _t)
  children_names = ['xyz', 'uvw', 'mno', 'abc']
  children = [N(child_name, _t) for child_name in children_names]
  _n.add_children(children)
  return all([c.name in children_names for c in _n.children])
