#hw3.py
# Peter Podniesinski + ppodnies + H

"""
   ** Place your manually-graded (Reasoning Over Code) solutions here! **
"""

######################################################################
# Place your non-graphics solutions here!
######################################################################
import random

def encodeRightLeftRouteCipher(plaintext, rows):
    text=plaintext
    order=ord('z')
    encrypt=""
    i=0
    if(len(plaintext)% rows!=0):
      col= len(plaintext)/rows +1 #adjusts for truncation
    else:
      col= len(plaintext)/rows
    while len(text) % rows != 0:
        text+=chr(122-i) #add on lowercase letters starting from z 
        i=(i+1)%26
    for i in xrange(rows): # if statement for switching back and forth
        if (i%2==0):
            for x in xrange(col): #encode left to right
                encrypt+=text[x*rows+i]
        else:
            for x in xrange(col): #encode right to left
                encrypt+=text[len(text)-rows+i-(x*rows)]
        
    return str(rows)+encrypt # concat row to front of string
#print encodeRightLeftRouteCipher('WEATTACKATDAWN', 4)
#print encodeRightLeftRouteCipher('AFSTINMWYFXTLNWDJAOIKHJMXMTWOY', 2)

def removeLowerCaseCharacters(encoding):
   text=encoding
   i=0
   while i< len(text):   
       if(ord(text[i])<=122 and ord(text[i])>=97): #between z and a
            text=text[0:i]+text[i+1:len(text)-1] #strips out lowerase letters
            i=0
       else:
           i+=1
   return text

def reverseString(string):
    reverse = ""
    for index in string:
        reverse = index + reverse
    return reverse

def reverseOddRow(plaintext,col):
   reverse=""
   index=0
   row=0
   while index < len(plaintext):
        if row % 2 != 0:
            reverse += reverseString(plaintext[index:index+col]) # reverses odd rows
        else:
            reverse += plaintext[index:index+col]
        index += col
        row += 1
   return reverse

def removeDigits(plaintext):
    text=plaintext
    i=0
    while i< len(text):
        if(ord(text[i])>=48 and ord(text[i])<=57):
            text=text[1:]
            i=0
        else:
            i+=1
    return text

def numRows(plaintext):
    text=plaintext
    rowCount=""
    i=0
    while i< len(text):
        if(ord(text[i])>=48 and ord(text[i])<=57):
            rowCount+=text[i:i+1]
            i+=1
        else:
            i+=1
    return int(rowCount)

#print numRows('10DDBLCFTKPPPXUAIYRKUBGYJOBRDKHL')

def decodeRightLeftRouteCipher(encoding):
   text=removeDigits(encoding)
   #this will strip out leading digit
   decode=""
   rows=numRows(encoding)
   if(len(text)% rows!=0):
      col= len(text)/rows #adjusts for truncation
   else:
      col= len(text)/rows
   reverse=reverseOddRow(text,col)#reverse odd rows
   for x in xrange(col):
      for y in xrange(rows):
         decode+=reverse[y*col+x]
   #decode=encodeRightLeftRouteCipher(text,rows)
   decrypted=removeLowerCaseCharacters(decode)
   return decrypted

print decodeRightLeftRouteCipher('10DDBLCFTKPPPXUAIYRKUBGYJOBRDKHL')
print decodeRightLeftRouteCipher('4WTAWNTAEACDzyAKT')
print decodeRightLeftRouteCipher('2CMISZVWJLBRDGAESNSBYUSYTRUFRFQ')
#print decodeRightLeftRouteCipher('10DDBLCFTKPPPXUAIYRKUBGYJOBRDKHL')
          
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

def isPalindrome(n):
   if n<0 :
      return False
   elif n>0 and n<10 and isPrime(n):
       return True
   elif n<100 and isPrime(n) and (n/10 == n%10):
       return True
   else:
       return type(n)==int and n>=0 and (n/100 == n%10)and isPrime(n)

for x in range(0,500):
    if(isPalindrome(x)):print x, isPalindrome(x)




def isPalindromicPrime(n):
   return (isPrime(n) and isPalindrome(n))

def nthPalindromicPrime(n):
    if(n<0):
        return 0
    index=0
    count=0
    while count <=n:
        index +=1
        if(isPalindromicPrime(index)==True):
            count+=1
    return index

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
        index+=1
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

def isSmithNumber(n):
   if(n<0):
      return 0
   if(isPrime(n)==True):
       return False
   elif(sumOfDigits(n)==primeFactorization(n)):
      return True
   else:
      return False

def nthSmithNumber(n):
    if(n<0):
        return 0
    index=0
    count=0
    while count <=n:
        index +=1
        if(isSmithNumber(index)==True):
            count+=1
        
    return index

def findZeroWithBisection(f,x0,x1,epsilon):
    if(f(x0)<0 or f(x1)<0) and (f(x1)>0 and f(x0)>0): #exactly one is negative
        return NONE
    xmid=(x0+x1)/2.0
    if (f(xmid)==0):
        return xmid
    while (x1-x0)>= epsilon:
         xmid=(x0+x1)/2.0
         if (f(xmid)>=0 and f(x0)>=0) or (f(xmid)<=0 and f(x0)<=0): #same sign
             x1=x1
             x0=xmid
         else:
             x1=xmid
             x0=x0
    return xmid


######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

######################################################################
# Place your (optional) additional tests here
######################################################################

def runMoreStudentTests():
    print "Running additional tests...",
    def testEncodeRightLeftRouteCipher():
       print "testing EncodeRightLeftRouteCipher"
       assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",4)=="4WTAWNTAEACDzyAKT")
       assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",6)=="6WCWNKEAAzyTTTDxwAA")
       print "passed"

    def testDecodeRightLeftRouteCipher():
       print "testing EncodeRightLeftRouteCipher"
       assert(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT",4)=="WEATTACKATDAWN")
      #assert(decodeRightLeftRouteCipher("WEATTACKATDAWN",6)=="6WCWNKEAAzyTTTDxwAA")
       print "passed"

    """def testFindZeroWithBisection():
       print" testing find bisection"
       assert(findZeroWithBisection("""

    def testIsSmithNumber():
       print "print testing smith numbers"
       assert(isSmithNumber(22)==True)
       assert(isSmithNumber(4)==True)
       assert(isSmithNumber(378)==True)
       assert(isSmithNumber(0)==False)
       assert(isSmithNumber(-2)==False)
       assert(isSmithNumber(223242)==False)

    def testNthSmithNumber():
        print "testing nthsmithnumber"
        assert(nthSmithNumber(0)==4)
        assert(nthSmithNumber(2)==4)
        assert(nthSmithNumber(3)==7)
        assert(nthSmithNumber(6)==131)

    def testNthPalindromicPrime():
       print "testing nth palindrome"
       assert(nthPalindromicPrime(0)==2 )
       assert(nthPalindromicPrime(1)== 3)
       assert(nthPalindromicPrime(-1)==0 )
       assert(nthPalindromicPrime(5)== 101)

    print "Passed them all!"

######################################################################
# Place your graphics solutions here!
######################################################################

from Tkinter import *
import math

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def randomCircleFun(canvas, left, top, width, height):
   #creates an image with random circles scattered with different sizes
   #and colors
   for outercirce in range(0,600):
       cx = random.randint(left,width)#random center
       cy = random.randint(top,height)
       #generates a random radius for an outer circle
       outerRadius= min (width,height) / (random.randint(12,40)) #seemed to be appropriate variables that satisfied sizes
       innerRadius= outerRadius
       #generates random rgb value between 0 and 256
       fill=rgbString(random.random() * 256,random.random() * 256,random.random() * 256) #color of circle, 256 rgb values
       canvas.create_oval(cx-outerRadius, cy-outerRadius,
                          cx+outerRadius, cy+outerRadius,fill=fill,width=0)# creates outer circle
       while innerRadius >= 0:
           #creates inner circles until it reaches
           fill=rgbString(random.random() * 256,random.random() * 256,random.random() * 256) 
           cx1=cx-innerRadius
           cx2=cx+innerRadius
           cy1=cy-innerRadius
           cy2=cy+innerRadius
           canvas.create_oval(cx1, cy1,       #outercircle radius
                             cx2, cy2,fill=fill,width=0)
           innerRadius-= min (width,height) / (random.randint(100,200)) #increments 

######################################################################
# Drivers: do not modify this code
#####################################################################

def onButton(canvas, drawFn):
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
    canvas.data.drawFns = [randomCircleFun]
    canvas.data.drawFn = canvas.data.drawFns[0]
    for i in xrange(len(canvas.data.drawFns)):
        drawFn = canvas.data.drawFns[i]
        b = Button(buttonFrame, text=drawFn.__name__, command=lambda drawFn=drawFn:onButton(canvas, drawFn))
        b.grid(row=0,column=i)
    canvas.pack()
    buttonFrame.pack()
    redrawAll(canvas)
    root.mainloop()

######################################################################
# Main: you may modify this to run just the parts you want to test
######################################################################

def main():
    # include following line to autograde when you run this file
    #execfile("hw2-public-grader.py", globals())
    runMoreStudentTests()
    graphicsMain()

if __name__ == "__main__":
    main()
