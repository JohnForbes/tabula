from hak.one.number.int.is_a import f as is_int
from hak.one.number.int.primes.prime_factors.get import f as get_prime_factors
from hak.pf import f as pf
from hak.pxyz import f as pxyz

div_int_by_rate = lambda u, v: Rate(u, 1, {'1': 0}) / v

def _g(a, b):
  if isinstance(a, float):
    decimal_place_count = len(str(a).split('.')[1].rstrip('0'))
    b *= 10**decimal_place_count
    a *= 10**decimal_place_count
    b = int(b)
    a = int(a)
  return a, b

class Rate:
  def __init__(self, numerator, denominator, unit):
    numerator, denominator = _g(numerator, denominator)
    denominator, numerator = _g(denominator, numerator)

    # if numerator == 0: denominator = 1

    # if is_int(numerator) and is_int(denominator):
    #   numerator_str = str(numerator)
    #   denominator_str = str(denominator)
    #   if all([
    #     numerator_str[-1] == '0',
    #     denominator_str[-1] == '0',
    #     len(numerator_str) > 1,
    #     len(denominator_str) > 1,
    #   ]):
    #     return Rate(int(numerator_str[:-1]), int(denominator_str[:-1]), unit)

    # if '.' in f'{numerator}{denominator}':
    #   p = len(str(numerator).split('.')[1]) if '.' in str(numerator) else 0
    #   q = len(str(denominator).split('.')[1]) if '.' in str(denominator) else 0
    #   u = max(p, q)
    #   factor = 10**u
    #   numerator == factor
    #   numerator = round(numerator)
    #   denominator == factor
    #   denominator = round(denominator)

    # if int(numerator) == numerator: numerator = int(numerator)
    # if int(denominator) == denominator: denominator = int(denominator)

    # if isinstance(numerator, dict):
    #   numerator = numerator['numerator']/numerator['denominator']

    if isinstance(numerator, float):
      decimal_place_count = len(str(numerator).split('.')[1].rstrip('0'))
      numerator *= 10**decimal_place_count
      denominator *= 10**decimal_place_count
      numerator = int(numerator)
      denominator = int(denominator)

    self.numerator = numerator
    self.denominator = denominator
    self.unit = unit
    self.simplify()

  def simplify(self):
    numerator = self.numerator
    denominator = self.denominator
    unit = self.unit

    npf = get_prime_factors(numerator)
    dpf = get_prime_factors(denominator)

    common_factors = set(npf.keys()).intersection(set(dpf.keys()))

    while common_factors:
      common_factor = common_factors.pop()
      numerator //= common_factor
      denominator //= common_factor
      npf = get_prime_factors(numerator)
      dpf = get_prime_factors(denominator)
      common_factors = set(npf.keys()).intersection(set(dpf.keys()))
    self.numerator = numerator
    self.denominator = denominator
    self.unit = unit

  n = property(lambda self: self.numerator)
  d = property(lambda self: self.denominator)

  def __add__(u, v):
    if u.unit != v.unit:
      raise ValueError(f"u.unit: {u.unit} != v.unit: {v.unit}")
    return Rate(u.n * v.d + v.n * u.d, u.d * v.d, u.unit)

  def __truediv__(u, v):
    _unit = {k: 0 for k in sorted(set(u.unit.keys()) | set(v.unit.keys()))}

    for k in u.unit: _unit[k] += u.unit[k]
    for k in v.unit: _unit[k] -= v.unit[k]

    unit = {k: _unit[k] for k in _unit if _unit[k] != 0}

    return Rate(u.numerator*v.denominator, u.denominator*v.numerator, unit)

  def __str__(self):
    if self.denominator == 0: return f"undefined"
    if self.numerator == 0: return f""
    if self.denominator == 1: return f"{self.numerator}"
    return f"{self.numerator}/{self.denominator}"

  def __sub__(u, v):
    if u['unit'] != v['unit']:
      raise ValueError(f"u['unit']: {u['unit']} != v['unit']: {v['unit']}")
    return Rate(u.n * v.d - u.d * v.n, u.d * v.d, u.unit)

  def __mul__(u, v):
    _unit = {k: 0 for k in sorted(set(u.unit.keys()) | set(v.unit.keys()))}

    for k in u.unit: _unit[k] += u.unit[k]
    for k in v.unit: _unit[k] += v.unit[k]

    return Rate(
      u.numerator  *v.numerator,
      u.denominator*v.denominator,
      {k: _unit[k] for k in _unit if _unit[k] != 0}
    )

  def __eq__(u, v):
    _u = Rate(u.n, u.d, u.unit)
    _v = Rate(v.n, v.d, v.unit)
    return all([_u.n == _v.n, _u.d == _v.d, _u.unit == _v.unit])
  
  __abs__ = lambda s: Rate(abs(s.numerator), abs(s.denominator), s.unit)
  __float__ = lambda self: self.numerator / self.denominator

f = lambda numerator, denominator, unit: Rate(numerator, denominator, unit)

def t_simplifies_at_init():
  x = {'numerator': 120, 'denominator': 240, 'unit': {'$': 1, 'm': -1}}
  y = f(1, 2, {'$': 1, 'm': -1})
  z = f(**x)
  return pxyz(x, y, z)

def t_numerator_float():
  x = {'numerator': 0.120, 'denominator': 240, 'unit': {'$': 1, 'm': -1}}
  y = f(1, 2000, {'$': 1, 'm': -1})
  z = f(**x)
  return pxyz(x, y, z)

def t_denominator_float():
  x = {'numerator': 120, 'denominator': 0.240, 'unit': {'$': 1, 'm': -1}}
  y = f(500, 1, {'$': 1, 'm': -1})
  z = f(**x)
  return pxyz(x, y, z)

def t_a():
  x = {'numerator': 1, 'denominator': 2, 'unit': {'$': 1, 'm': -1}}
  y = '1/2'
  z = str(f(**x))
  return pxyz(x, y, z)

def t():
  if not t_simplifies_at_init(): return pf('!t_simplifies_at_init')
  if not t_numerator_float(): return pf('!t_numerator_float')
  if not t_denominator_float(): return pf('!t_denominator_float')
  if not t_a(): return pf('!t_a')
  return 1
