# ignore_overlength_lines
# from .fn.to_fn_applied_to_sorted_keys_of_records import f as records_and_fn_to_fn_applied_to_sorted_keys_of_records
from src.functions.dict.records_and_function.to_sorted_keys_of_records import f as records_and_fn_to_fn_applied_to_sorted_keys_of_records

# from .to_pad_k_branch import f as records_to_pad_k_branch
from src.functions.dict.records_and_field_name.to_pad_k_branch import f as records_to_pad_k_branch

# from archive.strings.to_table_row import f as cell_strings_to_table_row_string
from src.functions.strings.cell_strings.to_table_row import f as cell_strings_to_table_row_string

from hak.pxyz import f as pxyz
from hak.one.dict.rate.make import f as make_rate

# records_to_k_branch_row
f = lambda x: cell_strings_to_table_row_string(
  records_and_fn_to_fn_applied_to_sorted_keys_of_records({
    'records': x,
    'function': records_to_pad_k_branch
  }),
  ' '
)

_records = [
  {
    'prices': {
      'apples': make_rate(1, 4, {'$': 1, 'apple': -1}),
      'bananas': make_rate(1, 2, {'$': 1, 'banana': -1})
    },
    'volumes': {
      'applezzz': make_rate(1, 1, {'apple': 1}),
      'bananazzz': make_rate(2, 1, {'banana': 1}),
      'pearzzzzzz': make_rate(3, 1, {'pear': 1})
    },
    'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
  }, 
  {
    'prices': {
      'apples': make_rate(3, 4, {'$': 1, 'apple': -1}),
      'bananas': make_rate(1, 1, {'$': 1, 'banana': -1})
    },
    'volumes': {
      'applezzz': make_rate(4, 1, {'apple': 1}),
      'bananazzz': make_rate(5, 1, {'banana': 1}),
      'pearzzzzzz': make_rate(6, 1, {'pear': 1})
    },
    'zloops': {'zloop': make_rate(7, 1, {'zloop': 1})}
  }
]

def t():
  x = _records
  y = '|             prices |                           volumes | zloops |'
  z = f(x)
  return pxyz(x, y, z)
