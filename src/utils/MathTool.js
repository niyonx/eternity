const math = require('mathjs')

class MathTool {
  constructor () {
    this.parser = math.parser()
    this.initCustomFunction()
  }

  eval (exp) {
    return this.parser.evaluate(exp)
  }

  //  Add custom operator to our parser
  initCustomFunction () {
    //  this function is for testing only
    this.parser.set('addTwo', function (val) {
      return val + 2
    })

    this.parser.set('π', Math.PI)

    this.parser.set('e', math.e)
  }
}

export default MathTool
