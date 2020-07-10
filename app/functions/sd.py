from .power import power
from .sqrt import sqrt

def sd (*arg):
  mean = 0
  for i in range(len(arg)):
    mean += arg[i]
  mean = mean / len(arg)

  deviationSquare = 0 # init deviation_square (x-lambda)
  sum = 0 # sum [(x-lambda)^2]
  for i in range(len(arg)):
    deviationSquare = power(arg[i] - mean, 2)
    sum += deviationSquare

  # divide the sum of difference by number of inputs
  return sqrt(sum / len(arg))