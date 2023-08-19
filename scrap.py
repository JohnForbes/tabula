from hak.one.string.colour.tgfr import f as tgfr
from hak.pxyz import f as pxyz
from src.block.hstack import f as hstack
from src.block.spec.info.make import f as make_info_block
from src.block.spec.name.make import f as make_name_block
from src.block.to_str import f as block_to_str
from src.table.border.add_left_and_right import f as add_left_and_right

# from hak.one.dict.is_a import f as is_dict
# from src.block.vstack import f as vstack
# from src.misc.children_block.make import f as make_children_block
# from src.misc.g import f as g
# from src.misc.h import f as h
# from src.misc.parent_block.make import f as make_parent_block
# from src.misc.top_level_block_without_children.make import f as make_top_level_block_without_children
# from src.misc.val_block.make import f as make_val_block
# from src.misc.value_row_strings.get import f as get_value_row_strings
# from src.misc.values.get import f as get_values
# from src.misc.width.get import f as get_width

def f(x):
  # top_level_blocks = [
  #   (
  #     make_top_level_block_with_children(x, k) # 'Info'
  #     if is_dict(x[0][k]) else
  #     make_top_level_block_without_children(x, k) # 'Name'
  #   )
  #   for k in sorted(x[0].keys())[::-1]
  # ]
  # final_block = hstack(top_level_blocks)

  final_block = hstack([make_name_block(x, 'Name'), make_info_block(x, 'Info')])
  return add_left_and_right(block_to_str(final_block))

def t():
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

  y = '\n'.join([
    "|---------|-------------------------------------|",
    "|    Name |                                Info |",
    "|---------|-------------------------------------|",
    "|         | Age | Country |          Appearance |",
    "|---------|-----|---------|---------------------|",
    "|         |     |         | Eye Colour | Height |",
    "|---------|-----|---------|------------|--------|",
    "|   Alice |  28 |     USA |      Green |   1.85 |",
    "|     Bob |  35 |  Canada |      Brown |   1.79 |",
    "| Charlie |  22 |      UK |       Blue |   1.62 |",
    "|---------|-----|---------|------------|--------|",
  ])

  z = f(x)
  return pxyz(x, y, z, new_line=1)

if __name__ == '__main__': print(tgfr(t()))
