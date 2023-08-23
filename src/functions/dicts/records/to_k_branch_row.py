# ignore_overlength_lines
from data.records import records_without_date as _records
from hak.pxyf import f as pxyf

from ...dict.records_and_field_name.to_pad_k_branch import f as f_a
from ...dict.records_and_function.to_sorted_keys_of_records import f as f_b
from ...strings.cell_strings.to_table_row import f as f_c

# records_to_k_branch_row
f = lambda x: f_c({
  'cell_strings': f_b({'records': x, 'function': f_a}),
  'col_separator_char': ' '
})

t = lambda: pxyf(
  _records,
  '|             prices |                           volumes | zloops |',
  f
)
