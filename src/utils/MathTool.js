// `include the custom function
import {ePower} from './functions/ePower'
import {mad} from './functions/mad'
import {power} from './functions/power'
import {sd} from './functions/sd'
import {sin} from './functions/sin'
import {tenPower} from './functions/tenPower'

// `include the math.js library
const math = require('mathjs')

class MathTool {
  constructor () {
    this.parser = math.parser()
    this.angleMode = 'deg'
    this._initCustomFunction()
  }

  eval (exp, angleMode) {
    return this.parser.evaluate(exp)
  }

  //  Add custom operator to our parser
  _initCustomFunction () {
    let self = this

    this.parser.set('ePower', function (num) {
      return ePower(num)
    })

    this.parser.set('tenPower', function (num) {
      return tenPower(num)
    })

    this.parser.set('sin', function (num) {
      return sin(num, self.angleMode)
    })

    this.parser.set('power', function (x, y) {
      return power(x, y)
    })

    this.parser.set('MAD', function () {
      return mad(...arguments)
    })

    this.parser.set('σ', function () {
      return sd(...arguments)
    })

    this.parser.set('π', Math.PI)

    this.parser.set('e', math.e)
  }
}

export default MathTool
