from hak.one.dict.get_max_depth import f as get_max_depth
from hak.one.list.interleave import f as interleave
from hak.pf import f as pf
from hak.pxyz import f as pxyz

from src.misc.g import f as g
from src.misc.h import f as h
from src.misc.value_row_strings.get import f as get_value_row_strings
from src.misc.values.get import f as get_values
from src.misc.width.get import f as get_width

# make_name_block
def f(x, k):
  values = get_values(x, (k,))
  w = get_width(k, values)
  b = h('-', w)
  q = [g(k, w), *[h(' ', w) for _ in range(get_max_depth(x[0], 0)-1)]]
  return [b, *interleave(q, b), b, *get_value_row_strings(values, w), b]

def t_2():
  x = [
    {"Name": "Alice", "Info": {"Age": 28, "Country": "USA"}},
    {"Name": "Bob", "Info": {"Age": 35, "Country": "Canada"}},
    {"Name": "Charlie", "Info": {"Age": 22, "Country": "UK"}},
  ]
  y = [
    "---------",
    "    Name ",
    "---------",
    "         ",
    "---------",
    "   Alice ",
    "     Bob ",
    " Charlie ",
    "---------",
  ]
  z = f(x, 'Name')
  return pxyz(x, y, z)

def t_3():
  x = [
    {
      "Name": "Alice",
      "Info": {
        "Age": 28,
        "Country": "USA",
        "Appearance": {"Eye Colour": 'Green', "Height": 1.85}
      },
    },
    {
      "Name": "Bob",
      "Info": {
        "Age": 35,
        "Country": "Canada",
        "Appearance": {"Eye Colour": 'Brown', "Height": 1.79}
      },
    },
    {
      "Name": "Charlie",
      "Info": {
        "Age": 22,
        "Country": "UK",
        "Appearance": {"Eye Colour": 'Blue', "Height": 1.62}
      },
    },
  ]
  y = [
    "---------",
    "    Name ",
    "---------",
    "         ",
    "---------",
    "         ",
    "---------",
    "   Alice ",
    "     Bob ",
    " Charlie ",
    "---------",
  ]
  z = f(x, 'Name')
  return pxyz(x, y, z)

def t_4():
  x = [
    {
      "Name": "Alice",
      "Info": {
        "Age": 28,
        "Country": "USA",
        "Appearance": {
          "Eye Colour": 'Green',
          "Height": 1.85,
          'Ears': {
            'height': 0.1,
            'width': 0.1
          }
        }
      },
    },
    {
      "Name": "Bob",
      "Info": {
        "Age": 35,
        "Country": "Canada",
        "Appearance": {
          "Eye Colour": 'Brown',
          "Height": 1.79,
          'Ears': {
            'height': 0.1,
            'width': 0.1
          }
        }
      },
    },
    {
      "Name": "Charlie",
      "Info": {
        "Age": 22,
        "Country": "UK",
        "Appearance": {
          "Eye Colour": 'Blue',
          "Height": 1.62,
          'Ears': {
            'height': 0.1,
            'width': 0.1
          }
        }
      },
    },
  ]
  y = [
    "---------",
    "    Name ",
    "---------",
    "         ",
    "---------",
    "         ",
    "---------",
    "         ",
    "---------",
    "   Alice ",
    "     Bob ",
    " Charlie ",
    "---------",
  ]
  z = f(x, 'Name')
  return pxyz(x, y, z)

def t():
  if not t_2(): return pf('!t_2')
  if not t_3(): return pf('!t_3')
  if not t_4(): return pf('!t_4')
  return True
