from functools import reduce

""" 
iterative approach to exponents
"""

def manual_exponent(num, exp):
  counter = exp - 1
  total = num

  while counter > 0:
    total *= num
    counter -= 1 

  return total

  """
  
  """