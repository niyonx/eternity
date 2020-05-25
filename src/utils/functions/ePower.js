import {factorial} from './factorial'

export function ePower (num) {
  let retained = 1
  let nominator
  let denominator
  let rounds = 40

  for (let i = 1; i <= rounds; i++) {
    nominator = Math.pow(num, i)
    denominator = factorial(i)
    retained = retained + nominator / denominator
  }

  return retained
}
