def PI():
  x = 2.0
  z = 2.0
  a = 1.0
  b = 3.0
  while (z > 1e-15):
    z = z * a / b
    x += z
    a += 1
    b += 2
  return x

# PI = 3.141592653589793
