import power from 'power.js'
import sqrt from 'sqrt.js'

export function sd () {

    var mean=0
    for (var i = 0; i < arguments.length; i++) {
      mean += arguments[i]
    }
    mean = mean/arguments.length

    
    var deviation_square=0 // init deviation_square (x-lambda)
    var sum=0 //sum [(x-lambda)^2]
    for (var i = 0; i < arguments.length; i++) {
        deviation_squar = power(arguments[i]-mean, 2)
        sum += deviation_square
    }

    //divide the sum of difference by number of inputs
    return sqrt(sum/arguments.length)
}
