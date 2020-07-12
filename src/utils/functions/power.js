// import {abs} from './abs.js'
// import {ePower} from './ePower.js'

// export function power (num, exponent) {
//   let result = 1
//   let absExponent = abs(exponent)
//   if (absExponent % 1 !== 0) {
//     let decimalExponent = absExponent % 1
//     let wholeExponent = absExponent - decimalExponent
//     result = power(num, wholeExponent) * ePower(decimalExponent * myln(num))
//   } else {
//     for (let i = 1; i <= absExponent; ++i) {
//       result = result * num
//     }
//   }

//   if (exponent < 0) {
//     return 1 / result
//   } else {
//     return result
//   }
// }

// export function myln (num) {
//   let rounds = 300
//   let temp = ((num - 1) / (num + 1))
//   let result = 0
//   for (let i = 1; i < rounds * 2; i += 2) {
//     let j = 1 / i
//     result = result + (j * power(temp, i))
//   }
//   return (2.0 * result)
// }
