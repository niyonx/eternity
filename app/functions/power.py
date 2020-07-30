from .abs import abs

def power (num, exponent):
  from .ePower import ePower
  result = 1
  absExponent = abs(exponent)
  if (absExponent % 1 != 0):
    decimalExponent = absExponent % 1
    wholeExponent = absExponent - decimalExponent
    result = power(num, wholeExponent) * ePower(decimalExponent * myln(num))
  else:
    for i in range(1,absExponent+1):
      result = result * num

  if (exponent < 0):
    return 1 / result
  else:
    return result

def myln(num):
  rounds = 300
  temp = ((num - 1) / (num + 1))
  result = 0
  for i in range(1,rounds*2,2):
    j = 1 / i
    result = result + (j * power(temp, i))
  return (2.0 * result)