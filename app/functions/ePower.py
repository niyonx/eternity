from .factorial import factorial

def ePower (num):
  from .power import power
  retained = 1
  nominator = 0
  denominator = 0
  rounds = 40

  for i in range(1,rounds+1):
    nominator = power(num, i)
    denominator = factorial(i)
    retained = retained + nominator / denominator
    
  return retained
