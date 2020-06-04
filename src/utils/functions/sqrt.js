import {abs} from './abs'

export function sqrt (num) {
  let result = num
  let last
  do {
    last = result
    result = (result + num / result) / 2
  } while (abs(result - last) > 0.00000001)
  return result
}
