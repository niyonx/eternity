import {ePower} from '../../../src/utils/functions/ePower'

test('test ePower(1)', () => {
  expect(parseFloat(ePower(1).toFixed(10))).toBe(2.7182818285)
})

test('test ePower(2)', () => {
  expect(parseFloat(ePower(2).toFixed(10))).toBe(7.3890560989)
})
