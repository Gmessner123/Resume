setwd("~/Desktop/Ma3/HW 7")
quakes = read.table("SimplifiedEarthquakeCatalog2018.txt")#,header=T)
times = diff(quakes[,1])
hist(times)
mean(times)
sd(times)
plot(qexp(ppoints(times), rate=(1/125.6498)),
     sort(times), main="Exponential Q-Q Plot",
     xlab="Theoretical Quantiles", ylab="Sample Quantiles")
abline(a=0, b=1)
ks.test(times, pexp, rate=1/(125.6498))


times2 = times[times > 4]
hist(times2)
mean(times2)
sd(times2)
plot(qexp(ppoints(times2), rate=1/216.8625),
     sort(times2), main="Exponential Q-Q Plot",
     xlab="Theoretical Quantiles", ylab="Sample Quantiles")
abline(a=0, b=1)
ks.test(times2, pexp, rate=(1/216.8625))

c = 0
for(t in times2){
  if(t < 1600 && t >= 1400)
  c = c + 1
}
c
