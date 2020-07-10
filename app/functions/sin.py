from .factorial import factorial
from .power import power
from .PI import PI
from .abs import abs

def sin (num, rounds = 40):
  from app.api.MathTool import MathTool as mt
  if(mt.getInstance().angleMode == 'deg'):
    num = num * (PI() / 180.0)
  num = abs(num % (2 * PI()))
  retained = float(0)
  nominator = float(0)
  denominator = float(0)
  multiplier = float(0)

  for i in range(rounds):
    nominator = power(-1, i)
    denominator = factorial(2 * i + 1)
    multiplier = power(num, 2 * i + 1)
    retained = retained + nominator / denominator * multiplier

  return retained
