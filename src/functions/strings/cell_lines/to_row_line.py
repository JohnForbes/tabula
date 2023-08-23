from hak.pxyf import f as pxyf

from ..cell_strings.to_table_row import f as f_a

# cell_lines_to_row_line
f = lambda x: f_a({'cell_strings': x, 'char': '-'})

def t():
  x = ['-------', '--------', '--------', '---------', '----------', '------']
  y = '|---------|----------|----------|-----------|------------|--------|'
  return pxyf(x, y, f)
