def sumOfDigits(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n/10
    return sum

def isHarshadNumber(n):
   #tests if n is a harshad number
   if(n<10):
      return False
   elif n%sumOfDigits(n)==0:
      return True

#print isHarshadNumber(10)

def nthHarshadNumber(n):
    #returns nthHarshad
    number=1
    count=-1
    while count <=n:
        if(count==n):
            return number
        elif(isHarshadNumber(number)==True):
            count+=1
        if(count==n):
            return number
        number+=1

#print nthHarshadNumber(0)

def rangeHarshad(n):
   #this function will create an upperbound
   #for nearestHarshadNumber, which is the next
   #harshadNumber >n
   upperRange=0
   i=0
   while nthHarshadNumber(i)!=n+1:
      if(nthHarshadNumber(i)>n):
         return nthHarshadNumber(i)
      i+=1
      
#print rangeHarshad(12)      
        
def nearestHarshadNumber(n):
   i=0
   nearestHarshad=nthHarshadNumber(0)
   #variable to keep track of
   #nearestHarshad so far
   while i<=rangeHarshad(n):#rangeHarshad(n) is an upperbound
      if(isHarshadNumber(i)): #i is a harshadNumber
         if(abs(n-i))<abs(n-nearestHarshad):
            #tests if the difference is < the prior difference
            nearestHarshad=i
      i+=1
   return nearestHarshad

print nearestHarshadNumber(16)

