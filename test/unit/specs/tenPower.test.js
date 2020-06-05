import {tenPower} from '../../../src/utils/functions/tenPower'

test('test tenPower(1)', () => {
  expect(tenPower(1)).toBe(10)
})

test('test tenPower(2)', () => {
  expect(tenPower(2)).toBe(100)
})
