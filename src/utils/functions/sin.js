/* eslint-disable */

import {factorial} from './factorial';
import {BigNumber} from 'bignumber.js';
import {power} from './power';
import {PI} from './PI';

export function sin (num, angleMode, rounds = 40) {
  num = angleMode === 'deg' ? num * (PI / 180.0) : num;
  let retained = new BigNumber(0);
  let nominator = new BigNumber();
  let denominator = new BigNumber();
  let multiplier = new BigNumber();

  for (let i = 0; i < rounds; ++i) {
    nominator = power(-1, i);
    denominator = factorial(2 * i + 1);
    multiplier = power(num, 2 * i + 1)
    retained = retained.plus(nominator.dividedBy(denominator).multipliedBy(multiplier));
  }

  return retained;
}
