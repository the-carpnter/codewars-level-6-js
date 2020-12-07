function narcissistic(value) {
    var n = value.toString().length
    var num = value.toString()
    var sum = 0
    for (var i = 0; i < n; i++){
      a = Number(num[i])
      sum += a**n 
    }
    return sum == value
    
}
