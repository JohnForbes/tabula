# from archive.strings.to_table_row import f as cell_strings_to_table_row_string
from hak.pxyf import f as pxyf

from ..cell_strings.to_table_row import f as cell_strings_to_table_row_string

# cell_lines_to_row_line
f = lambda x: cell_strings_to_table_row_string({
  'cell_strings': x,
  'col_separator_char': '-'
})

def t():
  x = ['-------', '--------', '--------', '---------', '----------', '------']
  y = '|---------|----------|----------|-----------|------------|--------|'
  return pxyf(x, y, f)
