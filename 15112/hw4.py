#hw4.py
# Peter Podniesinski + ppodnies + H

"""
   ** Place your manually-graded (Reasoning Over Code) solutions here! **
   Practuce quiz3
   Quick answers:
   1.s="abcd"
     s[2]="z" #this will result in an error because you cannot assign variables
   2. Triple quotes act to comment out sections of codes
   3.Yes, because n is essentially never changed. It is simply converted to an int
   and the converted back to a string with the ord() operator
   4.int(s) is better because it simply returns the integer equivelant of the
   given string. If you give eval different parameters that are not integers
   the method could cause problems or attain odd errors
   5. s.lower() converts a string to all lowercase and s.islower()
   identifies if it is all lewercase
   6. s.isalpha() checks if all of the string is made up of characters. It
   returns false if there is punctuation or numbers
   7.("abc%de%7.2fg" % (12, 34.567)) evaluates to
   'abc12e  34.57g' #because the digits(12,34.567) are assigned integers/floats
   that are substituted into the string in the location of the modulo
   8.Magic numbers are randomly derived numbers that are not explained or intuitive
   which are used in code poorly because these numbers may either work for only
   specific cases or simply are bad style because you will not understand it in the future.
   9. Understand the problem- define the problem precisely before you begin coding so you
   understand the question
   Devise a plan- write out on paper your general approach to the problem. So it can be
   translated into code easily
   Carry out Plan- Translate your solution to code
   Revise and reflect- Check you solution. Make appropriate changes if necessary. Test
   properly
   10. Have a clear and concise plan, avoid making very long code. Write out your solution
   in a very detailed and understandable way so it is exactly clear what you have to do.

   Code Tracing
   1.import string
    def f(x, s):
    while (len(s[x:-x]) > 0):
        s = s[x:-x:max(1,len(s)/5)]
        x += 1
        print x, s
    print f(1, string.ascii_letters)

    *This will print out
    2blvFP
    3v

    because x=2,3 each time it prints out since it increments by 1.
    s=blvFP because it starts at s[1:-1] b then increments by len(s)/5 which
    is 50/5==10 so you get b, l, v , F, P
    then it goes through the loop a second time where s starts at s[2] which will now
    be v according to the last line of code. x = 3 at this point so it prints
    out 3v
    
    2.
    def g(s, t):
    u = ""
    for i in xrange(len(s)):
        for c in t:
            if (ord(s[i]) == 1+ord(c)):
                print i, s[i], c
                u += s[i]
    return u
    print g("abcde", "cat")

    * This will print out
    1 b a
    3 d c
    bd

    Because, it will print out i, s[i], c when ord(s[i])==1+ord(c) this occurs
    here, ord('b')==1+ord('a') and will also occur once more when i ==3 at
    ord('d')==1+ord('c')

    u prints out bd because u is equal to s[i] which was b the first for loop then
    d the next time

    Reasoning Over Code

def f(x, y, z):
    assert((y - x) % z == 0)
    s = ""
    for n in xrange(x, y, z):
        offset = (n - ord('a')) % 26
        s += chr(ord('A') + offset)
    return (s == "VAF")

    1. This function will be satisfied by the values x=118,y=132,z=5
    I derived these values by tracing through the code and figuring out that
    chr(ord('A')+offset) had to equal V. Therefore, I computed that offset had to be
    equivelant to 21 then I pluged 21 into the offset equation and progressed from there.

def g(s):
    t = ""
    while (len(s) > 0):
        t += s[0]
        s = s[1:][::-1]
    return (t == string.digits)

    2.g("0246897531") returns true because it satisfies string.digits which
    requires t=="0123456789". The algorithm s=s[1:][::-1] means that each time you go
    through the loop s =s[1:] and the next time s will equal s=s[::-1] so it switches
    back and forth /everyother. 
    

    **QUIZ 3
    
   Quick Answers
   1.("a%%bc%de%6.1fg" % (123, 45.67))  evaluates to 'a%bc123e  45.7g' because
   the value 123 is substituted for %d since that is the formating syntax and
   %f is decimal dormal which gets replaced by the floating number
   2.Magic numbers are randomly derived numbers that are not explained or intuitive
   which are used in code poorly because these numbers may either work for only
   specific cases or simply are bad style because you will not understand it in the future.

   Code Tracing [20 pts]

Indicate what each will print:

import string
def f(x, s):
    while ((x < len(s)) and (s[x] < s[-1-x])):
        s = s[x:len(s):3]
        x += 1
        print x, s
print f(0, "abcde"*3)
1.will print out
1 adbec
2dc

Because it will print out x,s which x==1 through the first iteration
and s= adbec because s will go through the string abcdeabcdeabcde from [0:len(s)]
in intervals of 3. Then in the second iteration the same algorithm will
occur so it will start at s[1] since x has not incremented thus far and
will proceed to s[4] since it increments by 3 again.

def g(s):
    u = ""
    for i in xrange(len(s)):
        for k in xrange(i+1, len(s)):
            if (ord(s[k]) == i + ord(s[i])):
                print i, k
                u += s[i] + s[k]
    return u
print g("abcbcde")

2.will print out
1 2
1 4
2 6
3 6
bcbccebe

What this code basically does is complies all the characters in the
string where in the first iteration s[k] has an order i larger than s[i] or
1 larger since i==1. Therefore satisfiable values include b,c with index's
1,2 respectively and then again b,c with index 1,4.Then when i==2 s[k]
must equal 2+ord(s[2]) which is 2+ord('c') meaning that s[k] must be 2 characters
after c so 2,6 works. Then when i==3 s[k] must be 3 characters after b which
is e. so 3,6 works

Reasoning Over Code [20 pts]

Find arguments for the following functions that make them return True.

import math
def f(s):
    assert(type(s) == str)
    x0 = 0
    x1 = 100
    epsilon = 0.0001
    while (abs(x1 - x0) > epsilon):
        xmid = (x1 + x0)/2.0
        y = 10*xmid - 2*math.pi  # 3.14159265358...
        if (y > 0):
            x1 = xmid
        else:
            x0 = xmid
    t = "%0.2f" % ((x1 + x0)/2)
    return (s == t)

    1.originally xmid=50 then y=500-2*3.14 which is about  493.6
    therefor y>0 so s1=50 now xmid=244 about and this continues so on
    xmid=12.5 y=119
    xmid=6.25 y=62.5-6.28
    xmid=3.125 y=31.25-6.28
    xmid=1.56 y=15.6-6.28
    xmid=.78 y=7.8-6.28
    then xmid=.39 and y is less than 0 so
    x0 will equal .39 and x1 =.78
    and the final steps in the while loop should be
    xmid=.585 since y will be less than 0 x0=.585
    xmid now=.6825. This value will make y >0 since xmid is >2*pie
    so x1=.6825
    ** The final step will take the middle of x0 and x1 making
    xmid = 0.63
    This should be the final answer which is basically the decimal approximation
    to the hundredths digit of 2pie. 

def g(s):
    t = ""
    for i in xrange(5):
        t = (chr(ord('H')+i) * i) + t
    return (s == t)

    2. s must = "LLLLKKKJJI" because ...
    I will be the first character in the string at i==1 because chr(ord('H'))+0)*0
    will return nothing. Therefore when i=1 t=I. and from there when i=2 chr(ord('H')
    +2 will equal J and from there we can t adds 2 JJ's because it is multiplied by
    i which is 2. so t=JJ+t which is JJ+I so t=JJI and when i=3 t=KKKJJI


    **QUIZ 5
    f1. f1(6,2,2)
        because len(s)==6 since the tab acts as one index and a backslash
        deletes the character after it .
        k=2 because the index of the tab is 2
        x=2 because s.find returns 1 if the string finds the character and -1 if it doesnt
        so 1=-1+2
    f2.f2("%+dabc%0.1f") because %+d adds the first integer specified in that
    location including the correct sign and %0.1f substitutes the float in rounded to 0.1
    decimal

    f3. f3("degjn") because (ord(s[i]) MUST== (i + ord(s[i-1])))and i increments by 1
    each time. Therefore the difference between letters increases by 1 each time
    so you get degjn which has a respective difference of  1,2,3,4

    f4
    def f4(s,t):
    return (t[2] == str(len(t))) and (s[1:len(s)] == t[4:0:-1]) #t[2] has to be number
                                                            #since its the str of an int
   #len(t) has to be less than 10 since t[2] is one index place holder not 2 or more
   #len(s)=5 because s[1:len(s)] has to be  equivelant to t[4:0] which has a length of 4
   #f4(f4("23456", "76543")) will suffice as there is a variety of answers because t[2] had
   #to equal 5 since 5==str(len(t)) and then basically s and t are reversed so that
   #s[1]has to equal t[4] 

print f4("23456", "76543")

    f5. ("34a") is a viable solution because s[0] and s[1] has to equal
    3,4 since t will concatonate 3 on, then a - then go through the loop once
    again and concatonate a 4 onto it then a -. since (s[2]=='a') which is a
    character str(int(s[i])) will return an error so it will enter the except loop
    and add on str(2/2) then str(2/1) . Thus = "3-4-12"


    **F12 hw4b
    1.Selectionsort O(n**2)
    mergesort O(nlogn)
    linear search O(n)
    binary search O(log n)
    isPrime O(n)
    fasterIsPrime(n**0.5)

    2.1-1000= 10
    1-1billion=30
    1-1trillion=40

    3. (1,4,6,8) (2,3,5,7)

    4.(2,3,4,1,5)
      (2,3,1,4,5)
      (2,1,3,4,5)
      (1,2,3,4,5)

    5.foo(x) should be quadratic so big O is most likely O(nlogn)
    because the increase in runtime is clearly not exponential since as the
    input is doubled exponentially we should expect 4x the size(this is not so).
    We can conclude it is nlogn because 
    
    6.Confirm. I worked with selection sort and mergesort
    on xSortLab

    7.Selection sort
    The algorithm will go through comparisons in the following manner/amount
    n*n-1*n-2*n-3...*1 Which is basically the sumation of the numbers from
    1-n which is the equation n(n+1)/2 this evaluates to (n**2+n)/2 lower
    terms are droped and the notation is O(n**2)

    Merge sort

    in every level of the sort there is n steps. and the depth of the sort
    is log(n) because after each step the size of your groups is divided
    by 2. Start=n then n/2 then n/4 and so on this is log n
    Therefore you get n steps * log n depth evaluates to
    nlogn or a big oh O(nlogn)
    

    8.Bubble sort- i can conclude it should be O(n**2)
    array size=10000 time 1.913
    array size=20000 time 4.813
    array size=30000 time 9.452

    Quick sort-this sort must be O(nlogn) based on the results
    array size=10000 time 1.884
    array size=20000 time 4.966
    array size=30000 time 10.032

    9.
    A.2n+5= O(N)
    B.n+logn=O(n)
    C.N**3 + 45N**2 + 100logN=O(n**3)
    D.10n*3n=O(n**2)
    E.10n+3n=O(n)
    F.merge sort= O(nlogn)
    

    10. Worst case big Oh
    f0-O(n**2)
    f1-O(n**2)
    f2-O(n**2)
    f3-O(n**2)
    f4-O(logn)
    f5-O(nlogn)
    
"""

######################################################################
# Place your non-graphics solutions here!
######################################################################
import random
import math

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

def reverseOddRow(plaintext,col): #reverses chars in odd rows so that decode algorithm works
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

def removeDigits(plaintext): #removes Digit at begining of encoded plaintext so that
                                #you can decode in colomns simply
    text=plaintext
    i=0
    while i< len(text):
        if(ord(text[i])>=48 and ord(text[i])<=57):
            text=text[1:]
            i=0
        else:
            i+=1
    return text

def numRows(plaintext): #will calculate the correct amount of rows for the plaintext
                        #accounts for rows larger than 9
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
             #if f(xmid)>0 then you want to increase x0 by setting it equal to xmid
             x1=x1
             x0=xmid
         else:
             #not same sign or >0 so decrease x1 
             x1=xmid
             x0=x0
    return xmid

def match(s1,s2):
    for i in xrange(len(s1)):
        match=False
        for j in xrange(len(s2)):
            if(s1[i]==s2[j]): #if the ith character in s1 is equal to anycharacter in s2 set
                              #match=true
                match=True
        if(match==False): #if its false after the loop it means that no char in s2 equaled the the ith
                            #character in s1 so return false
            return False
    return True

def sameChars(s1,s2): 
   if(type(s1)!=str or type(s2)!=str):
      return False
   if(len(s1)==len(s2)==0):
      return True
   return (match(s1,s2) and match(s2,s1))
    
def hasBalancedParentheses(s):
    if(len(s)==0): #if length is 0 it is balanced
        return True
    leftCount=0
    rightCount=0
    while len(s)>0:
        if(rightCount>leftCount): #if there are more close parentheses then open you should return False
                                 # right away because the left parentheses will not be closed
            return False
        if(s[0]=="("):
            leftCount+=1
        elif(s[0]==")"):
            rightCount+=1
        s=s[1:]
    return (leftCount==rightCount) 

#print hasBalancedParentheses('This has no parentheses!')

def inverseF(y): #calls upon bisection function to approximate when f1 ==0
    y=y+.00001
    def f1(x):
        return 3**x-2**x-y
    return findZeroWithBisection(f1,0,100+math.log(abs(y)),0.001) #we use math.log(y) to set an
    #upper bound that will work for very large values, we have to add 100 since log(y)
    #will be too small for small values. We have to use abs and add one to y because
    #log(0) will return a domain error

print inverseF(0)

def islower(s):
    if(len(s)==0): #return False for length of 0
        return False
    lower=False
    for i in range(len(s)):
        if(ord(s[i])>97 and ord(s[i])<123): # range of all lower case char's from 'a' to 'z'
            lower=True
        if(ord(s[i])>=ord('A') and ord(s[i])<= ord('Z')):
            return False
    return lower

print islower("@#$#@abc")

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


######################################################################
# Drivers: do not modify this code
#####################################################################


######################################################################
# Main: you may modify this to run just the parts you want to test
######################################################################

def main():
    # include following line to autograde when you run this file
    #execfile("hw2-public-grader.py", globals())
    runMoreStudentTests()

if __name__ == "__main__":
    main()
