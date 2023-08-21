from hak.pxyz import f as pxyz

f = lambda x: '\n'.join(x)
def t():
  x = [
    "|---------|---------------|",
    "|    Name |          Info |",
    "|---------|-----|---------|",
    "|         | Age | Country |",
    "|---------|-----|---------|",
    "|   Alice |  28 |     USA |",
    "|     Bob |  35 |  Canada |",
    "| Charlie |  22 |      UK |",
    "|---------|-----|---------|",
  ]
  y = '\n'.join([
    "|---------|---------------|",
    "|    Name |          Info |",
    "|---------|-----|---------|",
    "|         | Age | Country |",
    "|---------|-----|---------|",
    "|   Alice |  28 |     USA |",
    "|     Bob |  35 |  Canada |",
    "| Charlie |  22 |      UK |",
    "|---------|-----|---------|",
  ])
  z = f(x)
  return pxyz(x, y, z)
