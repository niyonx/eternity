import {sd} from '../../../src/utils/functions/sd'

test('test sd(1, 2, 3, 4, 5)', () => {
  expect(parseFloat(sd(1, 2, 3, 4, 5).toFixed(10))).toBe(1.4142135624)
})
