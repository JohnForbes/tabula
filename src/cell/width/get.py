from src.cell.to_str import f as to_str
from src.cell.make import f as make_cell
from hak.pxyz import f as pxyz

# width
f = lambda x: len(to_str(x))

def t():
  x = make_cell(100)
  y = 3
  z = f(x)
  return pxyz(x, y, z)
