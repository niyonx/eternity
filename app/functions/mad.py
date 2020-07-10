def mad(*arg):
  # calculate the mean of inputs
  mean = 0
  for i in range(0,len(arg)):
    mean += arg[i]
  mean = mean / len(arg)

  # sum up the difference between each number and mean
  deviation = 0
  sum = 0
  for i in range(0,len(arg)):
    deviation = arg[i] - mean
    if (deviation < 0):
      deviation = -deviation
    sum += deviation
    
  # divide the sum of difference by number of inputs
  return sum / len(arg)