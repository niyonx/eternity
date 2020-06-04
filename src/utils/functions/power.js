
export function power (num, exponent) {
  let result = 1
  for (let i = 1; i <= exponent; ++i) {
    result = result * num
  }
  return result
}
