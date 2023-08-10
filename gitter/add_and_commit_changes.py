from gitter.f_a import f as f_A
from gitter.f_m import f as f_M
from gitter.f_d import f as f_D

term_to_function = {' M': f_M, '??': f_A, ' D': f_D}

# process_changes
def f(d):
  for term in [' M', '??', ' D']:
    if term in d:
      _=sorted(d[term])[0]
      term_to_function[term](_)
