function nthFibo(n) {
  var a = 0
  var b = 1
  while (n-1>0){
    var x = b
    b = a +b
    a = x
    n -= 1
  }
  return a
}
