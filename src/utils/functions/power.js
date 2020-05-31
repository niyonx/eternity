/* eslint-disable */

import BigNumber from 'bignumber.js';

export function power (num, exponent) {
  let result = new BigNumber(1);
  for (let i = 1; i <= exponent; ++i) {
    result = result.multipliedBy(num);
  }
  return result;
}
