from .abs import abs
from .ePower import ePower


def power(num, exponent):
  result = 1
  abs_exponent = abs(exponent)
  if abs_exponent % 1 != 0:
    decimal_exponent = abs_exponent % 1
    whole_exponent = int(abs_exponent)
    result = power(num, whole_exponent) * ePower(decimal_exponent * my_ln(num))
  else:
    abs_exponent = int(abs_exponent)
    for i in range(1, abs_exponent + 1):
      result = result * num

  if exponent < 0:
    return 1 / result
  else:
    return result


def my_ln(num):
  rounds = 300
  temp = ((num - 1) / (num + 1))
  result = 0
  for i in range(1, rounds * 2, 2):
    j = 1 / i
    result = result + (j * power(temp, i))
  return (2.0 * result)
