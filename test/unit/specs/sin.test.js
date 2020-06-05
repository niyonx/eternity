import {sin} from '../../../src/utils/functions/sin'
import {PI} from '../../../src/utils/functions/PI'

test('test sin(90deg)', () => {
  expect(parseFloat(sin(90, 'deg').toFixed(10))).toBe(1)
})

test('test sin(pi rad)', () => {
  expect(parseFloat(sin(0.5 * PI, 'rad').toFixed(10))).toBe(1)
})
