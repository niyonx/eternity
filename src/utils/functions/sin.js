import {factorial} from './factorial'
import {power} from './power'
import {PI} from './PI'
import {abs} from './abs'

export function sin (num, angleMode, rounds = 100) {
  num = angleMode === 'deg' ? num * (PI / 180.0) : num
  num = abs(num % (2 * PI))
  let retained = 0
  let nominator = 0
  let denominator = 0
  let multiplier = 0

  for (let i = 0; i < rounds; ++i) {
    nominator = power(-1, i)
    denominator = factorial(2 * i + 1)
    multiplier = power(num, 2 * i + 1)
    retained = retained + (nominator / denominator * multiplier)
  }

  return retained
}
