makeHist <- function() {
  a = as.matrix(read.table("/Users/Grant/Desktop/Ma3/Random32.txt"))
  print(length(a))
  bins=seq(0.0,1.0,by=0.05)
  hist(a, breaks=bins, freq=FALSE)
}
makeHist2 <- function() {
  a = as.matrix(read.table("/Users/Grant/Desktop/Ma3/Random32.txt"))
  print(length(a))
  hist(a)
}
makecdf <- function() {
  a = as.matrix(read.table("/Users/Grant/Desktop/Ma3/Random32.txt"))
  print(length(a))
  #hist(a)
  c = ecdf(a)
  plot(c)
}
calculateAvg <- function() {
  a = as.matrix(read.table("/Users/Grant/Desktop/Ma3/Random32.txt"))
  avg = 0
  for(num in a){
    avg = avg + num
  }
  avg = avg / length(a)
  return(avg)
}
calculateStDev <- function() {
  a = as.matrix(read.table("/Users/Grant/Desktop/Ma3/Random32.txt"))
  sum = 0
  avg = calculateAvg()
  for(num in a){
    sum = sum + (num - avg) * (num - avg)
  }
  return(sqrt(sum / (length(a) - 1)))
}


