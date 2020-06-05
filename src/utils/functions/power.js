import {abs} from './abs.js'

export function power (num, exponent) {
  let result = 1
  let absExponent = abs(exponent)
  for (let i = 1; i <= absExponent; ++i) {
    result = result * num
  }
  if (exponent < 0) {
    return 1 / result
  } else {
    return result
  }
}
