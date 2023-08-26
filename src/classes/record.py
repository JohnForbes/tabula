from hak.one.dict.is_a import f as is_dict

class Record:
  def __init__(self, x):
    if not is_dict(x): raise TypeError(f'not dict; x: {x}; type(x): {type(x)}')
    self.value = x
  
  __str__ = lambda self: str(self.value)

f = lambda: Record()
t = lambda: 1 # Functions externalised in functions directory
