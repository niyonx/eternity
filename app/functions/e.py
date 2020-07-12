# e = 1 + 1/1 + 1/2 + 1/3! + ... + 1/n! + ...

def E():
  result = 1
  denominator = 1
  for i in range(1,21):
    denominator = denominator * i
    result += 1 / denominator
  return result

# e = 2.718281828459045
