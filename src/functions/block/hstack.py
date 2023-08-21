from hak.pxyz import f as pxyz

# hstack
f = lambda x: ['|'.join([x_i[j] for x_i in x]) for j in range(len(x[0]))]

def t():
  u = [
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
  v = [
    "---------------",
    "          Info ",
    "-----|---------",
    " Age | Country ",
    "-----|---------",
    "  28 |     USA ",
    "  35 |  Canada ",
    "  22 |      UK ",
    "-----|---------",
  ]
  x = [u, v]
  y = [
    "---------|---------------",
    "    Name |          Info ",
    "---------|-----|---------",
    "         | Age | Country ",
    "---------|-----|---------",
    "   Alice |  28 |     USA ",
    "     Bob |  35 |  Canada ",
    " Charlie |  22 |      UK ",
    "---------|-----|---------",
  ]
  z = f(x)
  return pxyz(x, y, z, new_line=1)
