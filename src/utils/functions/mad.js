
export function mad () {

    //calculate the mean of inputs
    var mean=0
    for (var i = 0; i < arguments.length; i++) {
    	mean += arguments[i]
    }
  	mean = mean/arguments.length
  
    //sum up the difference between each number and mean
    var deviation=0
    var sum=0
    for (var i = 0; i < arguments.length; i++) {
        deviation=arguments[i]-mean
        if (deviation<0){
            deviation = -deviation
        }
        sum+=deviation
    }

    //divide the sum of difference by number of inputs
    return sum/arguments.length
  }
