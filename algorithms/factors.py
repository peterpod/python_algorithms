def isPrime(n): # from course notes % 5_-
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = int(round(n**0.5))
    for factor in xrange(2,maxFactor+1):
        if (n % factor == 0):
            return False
    return True
print(isPrime(7))

def sumOfDigits(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n/10
    return sum


def nthPrime(n):
    if(n<0):
        return -1
    index=0
    count=0
    while count <=n:
        index +=1
        if(isPrime(index)==True):
            count+=1
    return index
   
def primeFactorization(n):
   x=n
   multipleOfFactors=1
   sumOfFactors=0
   index=2
   while x>1:
       if(isPrime(index) and x%index==0):
          #multipleOfFactors=multipleOfFactors*nthPrime(index)
          sumOfFactors+=sumOfDigits(index)
          x/=index
          index=index
       else:
           index+=1
   return sumOfFactors

print primeFactorization(180)
      
      
      
