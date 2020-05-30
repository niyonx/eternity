export const PI = (function () {
  let x = 2
  let z = 2
  let a = 1
  let b = 3
  while (z > 1e-15) {
    z = z * a / b
    x += z
    a++
    b += 2
  }
  return x
})()
