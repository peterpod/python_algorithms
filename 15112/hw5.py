#hw5.py
# Peter Podniesinski + ppodnies + H

"""
   Reasioning About Code

   f1(s):f1("afkpu") basically what this function does is
   iterates j the length of the ascii lowercase letters and if
   j% len(s) == 0 or j%5 == 0 you add one to i. To solve this problem
   you must check when this is true. So it occurs when j is 0,5,10,1,20.
   Therefore, since s[i] must equal string.ascii_lowercase[j] "afkpu" is
   the answer since they mirror the appropriate index's.

   f2(a):f2([6,8,5,7])
   This is because,
   #sorted(a)=[5,6,7,8]
   #b[3]=0 since b[3]=b*i or b*0 when i=0 also b[2]=5(because its the minimum)
   #b[1]=7 b[0]==18 therefore a[0]=6 since its b[0]*=3
   #then a[2]==5 since its the min(a) . then the last 2 integers
   #are easy since a[1]>a[3] so a[1] must=8 and the other =7

   f3(x,y):
   #x=36, y=8. This is because you must
#satisfy the boolean constraints being y==1<<(x/10)
#first. This is a bitwise operator that does a left shift.
#the values above satisfy this because 1 left shift 3 will make
#1000 since this converted from binary to decimal is 8.
#the next case is satisfied by 8<<3 which is 1000 plus 3 more 0's
#this equals 1000000= 64. Thus 64+36=100

   f4(s): f4("ABCDDAD")
   #this means that the count for index 0,1,2,3 should be
   #2,1,1,3 respectively because of the assertion statement
   which says that ord(t[i])-ord("A")==s.count[i]
   so for i=0, ord(C)-ord(A)=2 so s.count must =2
   # also, every third element should equal s[5:2:-1] '
   Therefore, my solution works because the first index is repeated twice
   and s[0]==s[5]. while second/third only appears once. Now D is the s[3]
   as well as s[4] and s[6]

   f5(y):y=23
    #basically in this problem you must solely focus on the
   #return statement within the while loop because 2*y can never equal -y
   # therefore you loop through the while tracing what the code will do for each
   #x value. basically you must find an x value with only 2 factors 1 and itself
   #so the first prime under 28 which is 23. So x==23==y

   f6(n): answer= 8766
   I got to this solution by first realizing when r will attain a value of
   6 since inside that conditional is when the value of m will change.
   Then I figured out certain numbers that would help multiply r to 6. It is
   not possible to multiply straight to 6 since 5 is in the middle so the largest
   possible value for ord(c)-ord("5") is 5. Therefore, you would have to get to
   6 by multiplying by 2 or 3 first and then again vica versa. The next step
   is to find a value that results in r=6 so I found out 78 will work because 7 is
   2 from 5 and 8 is 3 from 5 so you get r*=2, r*=3. However, The loop iterates
   all the way to 10,000 so we need to find the largest possible value that can generate
   r=6. This will be 8766 since it cannot be > 9000 since this will automatically disqualify it
   because 6 has no factor of 5.

   f7(n,k,x):
   f7(6,2,2)
        because len(s)==6 since the tab acts as one index and a backslash
        deletes the character after it .
        k=2 because the index of the tab is 2
        x=2 because s.find returns 1 if the string finds the character and -1 if it doesnt
        so 1=-1+2

   f8(fmt):
   f8("%+dabc%0.1f") because %+d adds the first integer specified in that
    location including the correct sign and %0.1f substitutes the float in rounded to 0.1
    decimal

   f9(s):
   f9("degjn") because (ord(s[i]) MUST== (i + ord(s[i-1])))and i increments by 1
    each time. Therefore the difference between letters increases by 1 each time
    so you get degjn which has a respective difference of  1,2,3,4

   f10(s,t):
   #t[2] has to be number
   #since its the str of an int
   #len(t) has to be less than 10 since t[2] is one index place holder not 2 or more
   #len(s)=5 because s[1:len(s)] has to be  equivelant to t[4:0] which has a length of 4
   #f4(f4("23456", "76543")) will suffice as there is a variety of answers because t[2] had
   #to equal 5 since 5==str(len(t)) and then basically s and t are reversed so that
   #s[1]has to equal t[4] 

   Answer:("23456", "76543")

   f11(a):f11([1,"1",2,"3",4,"7",8,"15"])
   To get to this answer first I understood exactly what both the
   assertions were asking. First a[i] must always be > than s. So for
   example a possible a[0] could be 1 since 1>0 . Then it says that str(s)==
   a[i+1]. Therefore not only must they be equivilant but in the array.
   the a[i+1] element must always be a string. There for the first two
   element could be [1,"1"] Then you must basically repeat these steps
   with a[i] > s so next possibility is 2 since 2>1 and s=s+2 now so s=3
   therefore a[i+1] ="3" and so on.


   f12(a):
   #b is sorted and its basically the list of range(len(a)) .For example
    #range(4) is [0,1,2,3]. and so on. i is the index in a where b[1] occurs
    #then it basically says b[1],b[3],b[5] equal a[i],a[i+1],a[i+2] respectively
    # all this function requires then is for the values at those index's to be
    #equivelant therefore values at a[0],a[2],a[4] are not as important
    #a possible soultion is as follows
    #f12([0,1,3,5,2,4]), b would equal[0,1,2,3,4,5]

   TRUE OR FALSE
   a.True
   b.False
   c.False
   d.False
   e.True
   f.False
   g.True
   h.False
   i.False
   j.True

   Very Short Answers
   a.height bars:
   at this point (half way) you should have 4 lists
   each of which are sorted from smallest to largest. The last
   step is to combine the two.
      (1,3) (4,8) (2,3) (7,9)
   b.
   def f(s,t):
      if(s==t):
         return True
      else:
         return False

   c.1 billion elements should take 8 miliseconds

   d.
   fa(n):O(n**2)
   fb(n):O(n)
   fc(n):O(n**3)
   fd(n):O(nlogn)

   e. Short circuit evalutaion is the boolean process that can occur when you have
   boolean comparisons seperated by an and. So for example if(x) and (y):
   this means that if x is false then the python will not even evaluate y because by
   the defenition of an and, if one is false it cannot be true.
   
"""

######################################################################
# Place your non-graphics solutions here!
######################################################################
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
   if(isHarshadNumber(n)):
       #if n is already a harshadNumber i increment it by 1
       #so that the while loop will execute properly
       upperRange=n+1
   else:
       upperRange=n
   i=0
   while nthHarshadNumber(i)!=upperRange:
      if(nthHarshadNumber(i)>upperRange):
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

#print nearestHarshadNumber(16)

def alternatingSum(a):
   total=0
   for i in range(len(a)):
      if(i%2==0):#if index is even add the element in the list
         total+=a[i]
      else:#odd index subtracts the elements 
         total-=a[i]
   return total

#print alternatingSum([5,3,8,4])

def nameCountList(list):
   #helper function to organize the parameter of mostCommonName to
   #return the frequencies of each name
   nameCountList=[]
   nameCount=0
   if(len(list)==0):
      return None
   for i in range(len(list)):
      mostCommonName=list[i]
      for j in range(len(list)):
         if(mostCommonName==list[j]):
            nameCount+=1
      #create a list compiled of the count of each name in the original list
      nameCountList+=[nameCount]
      nameCount=0
   return nameCountList

#print nameCountList(["Jane","Aaron","Cindy","Aaron","Jane"])  

import copy
def mostCommonName(list):
   if(len(list)==0):
      return None
   elif(len(list)==1):
       return list[0]
   countList=nameCountList(list)
   biggestSoFar=0
   finalList=[]
   for index in range(len(countList)):
      if(countList[index]>biggestSoFar):
         #records the index of the largest element
         biggestSoFar=countList[index]
         finalList.append(list[index])
      elif(countList[index]==biggestSoFar):
         finalList.append(list[index])
      #when there are more then one common name
   a=[]
   for i in range(len(finalList)):
      for j in range(len(finalList)):
         if(finalList[i]==finalList[j]):
            if(a.count(finalList[i])==0):
               a.append(finalList[i])
   b=sorted(a)
   print len(b)
   if(len(b)>1):
       return b
   else:
       return b[0]

print mostCommonName(["aaron","jane","aaron"])
   

def reverse(a):
   #destructive function that reverses list but returns None
   for index in range(len(a)/2):
   #len(a)/2 because you only need to switch numbers up to middle index
      a[index],a[len(a)-index-1]=a[len(a)-index-1],a[index]
      #adds numbers to the front from the back of a
      #uses tuples to perform switch operation

#print reverse([2,1,0])

def vectorSum(a,b):
   assert(len(a)==len(b)) #makes sure length of vectors is the same
   vectorSum=[]
   for index in range(len(a)):
      sum=a[index]+b[index]
      #add the sum to Vector Sum
      vectorSum+=[sum]
   return vectorSum

#print vectorSum([2,4],[20,10])

def isSorted(a):
   if(len(a)<=1): #length <=1 is always sorted
      return True
   for index in range(1,len(a)):
      if(a[index]==a[index-1]):
          pass
      elif(a[0]>a[1]):
          if(a[index]<a[index-1]):
              pass
          else:
              return False
      elif(a[0]<a[1]):
          if(a[index]>a[index-1]):
              pass
          else:
              return False
   return True

print isSorted([1,1,2,1])

import copy
def duplicates(a):
   a=sorted(a)#sorts list with O(nlogn)
   duplicates=[]
   if(len(a)<=1):
      return []
   for i in range(1,len(a)):
      if(a[i]==a[i-1]):#if two adjacent elements are equal they are duplicates
            duplicates+=[a[i]]
   c=copy.copy(duplicates)
   for i in range(1,len(duplicates)):#remove duplicates in list duplicates
         if(duplicates[i]==duplicates[i-1]): 
            c.remove(duplicates[i])
   if(len(c)==0):
      return []
   return c
    
#print duplicates([1, 3, 5, 7, 9, 5, 3, 5, 3,7,7]) 

def dotProduct(a,b):
   dotProduct=0
   if(len(a)>len(b)):
      #if lengths are not equal use smaller length
      length=len(b)
   else:
      length=len(a)
   for index in range(length):
      product=a[index]*b[index]
      dotProduct+=product
   return dotProduct

#print dotProduct([1,2,3],[4,5,6])

def isRotation(a1,a2):
   if(len(a1)!=len(a2)):
       return False
   for i in xrange(len(a1)):
      #use an offset value to demonstrate shift
      offset=-i
      count=0
      for j in xrange(len(a1)):
         print 
         if(a1[j+offset]==a2[j]):
               rotation=True
               count+=1 
      if count==len(a1):
         #if count adds up to total length then offset is correct
         #and the two arrays are rotations
         return True
   return False

#print isRotation( [3,2,4,5,6], [4,5,6,2,3])

def subsetSum(a):
   return 42
   

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################



######################################################################
# Place your (optional) additional tests here
######################################################################
def runMoreStudentTests():
   print "Running additional tests..."
   
def testAlternatingSum():
    print "testing.. " ,
    assert(alternatingSum([5,3,8,4])==6)
    assert(alternatingSum([5,1,2,4])==2)
    assert(alternatingSum([0,3,8,4])==1)
    assert(alternatingSum([5,7,8,9])==-3)
    print "passed alternatingSum "
def testMostCommonName():
    print "testing.. ",
    assert(mostCommonName(["Jane", "Aaron", "Jane", "Cindy", "Aaron"])==["Aaron","Jane"])
    assert(mostCommonName(["Aaron", "Jane", "Cindy", "Aaron"])==["Aaron"])
    print "passed..mostCommonName "
def testReverse():
    print "testing.. reverse",
    assert(reverse([5,3,8,4])==None)
    assert(reverse([5,1,2,4])==None)
    assert(reverse([0,3,8,4])==None)
    print "passed.. reverse"

def testVectorSum():
    print "testing.. VectorSum",
    assert(vectorSum([2,4],[20,10])==[22,14])
    assert(vectorSum([0,2],[30,20])==[30,22])
    assert(vectorSum([8,12],[2,11])==[10,23])
    print "passed.. VectorSum"

def testIsSorted():
    print "testing.. isSorted",
    assert(isSorted([10,2,3,9])==False)
    assert(isSorted([1,2,3,9])==True)
    assert(isSorted([10,0,3,2])==False)
    assert(isSorted([0,2,3,24])==True)        
    print "passed.. isSorted"

def testDuplicates():
    print "testing.. Duplicates",
    assert(duplicates([1, 3, 5, 7,7]) ==[7])
    assert(duplicates([1, 3,3, 5, 7,7]) ==[3,7])
    assert(duplicates([1, 3, 5, 7]) ==[])
    assert(duplicates([1, 3, 5, 7,7,8,8]) ==[7,8])
    print "passed.. Duplicates"

def testDotProduct():
    print "testing.. DotProduct",
    assert(dotProduct([1,2,3],[4,5,6])==32)
    assert(dotProduct([1,2,1],[4,5,6])==20)       
    print "passed.. DotProduct"
def testIsRotation():
    print "testing.. isRotation ",
    assert(isRotation( [2,3,4,5,6], [4,5,6,2,3])==True)
    assert(isRotation( [3,2,4,5,6], [4,5,6,2,3])==False)
    assert(isRotation( [1,2,3,4], [2,3,4,1])==True)
    assert(isRotation( [0,1,2,3], [0,2,1,3])==False)
    assert(isRotation( [6,5,4,3,2,1], [4,3,2,1,6,5])==True)
    print "passed.. isRotation"
def SubsetSum():
    print "testing.. "
    print "passed.. "

###################################################################
# Place your graphics solutions here!
######################################################################

from Tkinter import *
#import math

######################################################################
# Drivers: do not modify this code
#####################################################################

"""def onButton(canvas, drawFn):
    canvas.data.drawFn = drawFn
    redrawAll(canvas)
    
def redrawAll(canvas):
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,canvas.data.width,canvas.data.height,fill="cyan")
    drawFn = canvas.data.drawFn
    if (drawFn):       
        drawFn(canvas, 0, 0, 800, 800)
        
        canvas.create_text(canvas.data.width/2,20, text=drawFn.__name__, fill="black", font="Arial 24 bold")

def graphicsMain():
    root = Tk()
    canvas = Canvas(root, width=750, height=500)
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width = 750
    canvas.data.height = 500
    buttonFrame = Frame(root)
    canvas.data.drawFns = []
    canvas.data.drawFn = canvas.data.drawFns[0]
    for i in xrange(len(canvas.data.drawFns)):
        drawFn = canvas.data.drawFns[i]
        b = Button(buttonFrame, text=drawFn.__name__, command=lambda drawFn=drawFn:onButton(canvas, drawFn))
        b.grid(row=0,column=i)
    canvas.pack()
    buttonFrame.pack()
    redrawAll(canvas)
    root.mainloop()"""

######################################################################
# Main: you may modify this to run just the parts you want to test
######################################################################

def main():
    # include following line to autograde when you run this file
    runMoreStudentTests()
    testAlternatingSum()
    testReverse()
    testVectorSum()
    testIsSorted()
    testDuplicates()
    testDotProduct()
    testIsRotation()  
    #testMostCommonName()
    #graphicsMain()

if __name__ == "__main__":
    main()
