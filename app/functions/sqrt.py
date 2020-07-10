from .abs import abs

def sqrt (num):
  result = num
  last = 0
  while True:
    last = result
    result = (result + num / result) / 2
    if not (abs(result - last) > 0.00000001):
        break
  return result