L <- function (p) (factorial(21+25+24+39))/(factorial(21)*factorial(25)*factorial(24)*factorial(39))* 
  (choose(3,0)**21)*(choose(4,1)**25)*(choose(5,2)**24)*(choose(6,3)**39)*
  (((p**4)*(1-p)**0 + (p**0)*(1-p)**4)**21)*(((p**4)*(1-p)**1 + (p**1)*(1-p)**4)**25)*
  (((p**4)*(1-p)**2 + (p**2)*(1-p)**4)**24)*(((p**4)*(1-p)**3 + (p**3)*(1-p)**4)**39)

LogL <- function (p) (log(L(p)))

curve( L(x), xlim=c(0,1), xlab="p",
       ylab="Log likelihood", main="Log of likelihood function")

curve( LogL(x), xlim=c(0,1), xlab="p",
       ylab="Log likelihood", main="Log of likelihood function")


print(optimize(LogL, interval=c(.5,1), maximum=TRUE ))

