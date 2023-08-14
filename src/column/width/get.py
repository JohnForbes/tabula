from hak.pf import f as pf
from hak.pxyz import f as pxyz
from src.column.make import f as make_column
from src.cell.make import f as make_cell

# width
f = lambda x: max(len(x['name']), *[len(str(c['value'])) for c in x['cells']])

def t_a():
  x = make_column('apples', [make_cell(_, 'apples') for _ in range(100)])
  y = 6
  z = f(x)
  return pxyz(x, y, z)

def t_cells_dominant():
  x = make_column('a', [make_cell(v, 'a') for v in [0, 1000, 2, 3]])
  y = 4
  z = f(x)
  return pxyz(x, y, z)

def t_name_dominant():
  x = make_column('abc', [make_cell(v, 'abc') for v in [0, 1, 2, 3]])
  y = 3
  z = f(x)
  return pxyz(x, y, z)

def t():
  if not t_a(): return pf('!t_a')
  if not t_name_dominant(): return pf('!t_name_dominant')
  if not t_cells_dominant(): return pf('!t_cells_dominant')
  return True
