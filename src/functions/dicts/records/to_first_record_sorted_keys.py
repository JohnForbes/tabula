from hak.one.dict.get_sorted_keys import f as get_sorted_keys
from hak.pxyf import f as pxyf

# records_to_first_record_sorted_keys
f = lambda x: get_sorted_keys(x[0])

t = lambda: pxyf([{'c': 0, 'b': 1, 'a': 2}, {}], list('abc'), f)
