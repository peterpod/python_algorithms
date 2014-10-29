import random

def make2dList(rows,cols):
   a=[]
   for row in xrange(rows): a += [[0]*cols]
   return a

def hiddenNumbers(rows,cols):
   hiddenNumbers=make2dList(rows,cols)
   maxNumber=(rows*cols)/2
   randomNumberCount=[0]*maxNumber
   print maxNumber, len(randomNumberCount)
   for row in xrange(rows):
      for col in xrange(cols):
         randomNumber=random.randrange(1,maxNumber+1)
         print randomNumber
         while randomNumberCount[randomNumber-1]>=2:
            #subtract 1 to avoid index out of range
            #makes sure you choose a number no more than twice.
            randomNumber=random.randrange(1,maxNumber+1)
         else:
            hiddenNumbers[row][col]=randomNumber
            randomNumberCount[randomNumber-1]+=1
   return hiddenNumbers

print hiddenNumbers(8,8)
