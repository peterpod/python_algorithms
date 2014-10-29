# hw9.py
# <ppodnies>, <H>

"""
1. I did it!(i studied)

Reasoning over code! 
 
def f(n):
   # assume n is a non-negative integer
   if (n < 10):
      return 1
   else:
      return 1 + f(n/10)

Answer, this function will return basically the count
of however many times n is divided by 10. so with the given
function f(100): the program will execute as following:
100 is not <10 so it returns 1+f(10), 10 is not < 10 so
it returns 1+f(1) which is = f(10). Then it reaches the
base case and returns 1. You trace back that f(1)=1 and f(10)=1+1
and finally f(100)=1+f(10) which = 1+2=3
 
def f(a):
   # assume a is a list of strings
   if (len(a) == 0):
      return ""
   else:
      x = f(a[1:])
      if (len(x) > len(a[0])):
         return x
      else:
         return a[0]
         
#Answer: this program is a recursive function that returns the
longest string within a list. Basically what it does is recurses
in the statement x = f(a[1:]) the function will recursively call itself
until it reaches the end of the list and if the largestString So far is
not greater than the first string, a[0], it will return the first.
 
def f(a):
   # assume a is a list of integers
   if (len(a) == 0):
      return 0
   elif (len(a) == 1):
      return (a[0] % 2)
   else:
      i = len(a)/2
      return f(a[:i]) + f(a[i:])

#Answer: This function takes in an array, if the array is empty is returns
simply 0. however, if it takes in a large array the recursive statments
recursive statements call itself twice, first with the first half of the
array plus the f of the second half of the array. This behavior is done
due to the statement: i=len(a)/2 which basically divides the array given in
two.  Therefore, the function will keep recursiving until the length of the array
is 1. where it takes the value, a[0] and mod's it by 2.

Essentially this program takes each int value in a list and sums of the mod 2
result of each value.

def f(n):
   # assume n is a non-negative integer
   if (n == 0):
      return 1
   else:
      return 2*f(n-1)

#Answer: this function basically returns 2 to the power of n or 2**n.
To prove this we test f(4). 4!=0 so we reach the recursive case where
we return 2* f(3). and so 3!=0 so we return 2*f(2) then 2!=0 so we return
2*f(1). we repead the recursive case one more time returning 2*f(0) which
finally returns 1. Thus, we trace this back to the top level call
where 2 is multiplied by itself 4 times

 
def f(n):
   # assume n is a non-negative integer
   if (n == 0):
      return 0
   else:
      return f(n-1) + 2*n - 1

#Answer: This function is a recursive function that takes in
an integer and returns n**2. So if you call f(2) you get 4. or if
you return f(3) you get 9. 

# Hint: you may want to try this function with a few sample values.
# The answer should quickly become apparent, though you may wish to
# think about why the answer is in fact what it is.
"""

########################
# YOUR CODE GOES HERE! #
########################
from Tkinter import *
import os

def flatten(a):
   #base case
   if(a==[]):
      return []
   elif(type(a)!=list):
      #if it is simply an int return the value
      return a
   elif(type(a[0])==type([])):
      return flatten(a[0])+flatten(a[1:])
   else:
      return [a[0]]+flatten(a[1:])


def findLargestFile(path):
   #if its just a file
   if(not os.path.isdir(path)):
      return path
   else:
      largestSoFar=""
      for sub in os.listdir(path):
         largest=findLargestFile(path+"/"+sub)
         if(largestSoFar=="" or(largest!="" and(os.path.getsize(largest)>
                              os.path.getsize(largestSoFar)))):
            largestSoFar=largest
      return largestSoFar

def solveABC(constraints,aLocation):
   board=[]
   d=dict()
   boardRow=len(constraints)
   row=5
   col=5
   for rows in range(row):board+=[["-"]*col]
   board[aLocation[0]][aLocation[1]]="A"
   rowList=[]
   colList=[]
   toprowString=""
   bottomrowString=""
   topcolString=""
   bottomcolString=""
   diagonalString=""
   diagonalListRight=[("C","G")]
   diagonalListLeft=[("V","S")]
   for rows in xrange(1,6):
      toprowString+=constraints[rows]
   for rows in xrange(13,18):
      bottomrowString+=constraints[rows]
   for cols in xrange(7,12):
      topcolString+=constraints[cols]
   for cols in xrange(19,24):
      bottomcolString+=constraints[cols]
   #make the rowList
   for index in xrange(row):
      #print index,row-index
      colList+=[(toprowString[index],bottomrowString[row-index-1])]
   for index in xrange(row):
      rowList+=[(topcolString[index],bottomcolString[row-index-1] )]  
   def isLegal(letter,previous, row, col):
        #check if on board
        if((row>4)or (row<0) or
           (col<0) or (col>4)):
           #print "out of bounds"
           return False
        #letter following it is sequential to the alphabet
        #is it 1 more than the letter preceeding it
        elif(ord(letter)!= ord(previous)+1):
           #print "not adjacent"
           return False
        #doesnot follow constraints
        #if letter is in rowlist at specific row
        elif(board[row][col]!="-"):
           return False           
        elif((letter==rowList[row][0])or(letter==rowList[row][1])):
           return True
        #check colList if its one of the tuples
        elif((letter==colList[col][0])or(letter==colList[col][1])):
              return True
        elif(row==col): #it leftRight diagonal
           #check diagonals"""
           #print "its diagonal"
           if(letter==diagonalListRight[0][0] or letter==diagonalListRight[0][1]):
              return True
        elif(row+col==4):
           if(letter==diagonalListLeft[0][0] or letter==diagonalListLeft[0][1]):
              return True
        return False        
        
   def solved(board):
      for row in xrange(len(board)):
         for col in xrange(len(board[0])):
            #if board still has default values it is not solved
            if(board[row][col]=="-"):
               return False
      return True
   
   def solve(board,letter, row, col):
      nextLetter=chr(ord(letter)+1)
      if(solved(board)==True):
         #it has all the correct values
         return board
      else:
         for rows in xrange(-1,2):
            for cols in xrange(-1,2):
               drow=row+rows
               dcol=col+cols
               if isLegal(nextLetter,letter,drow,dcol):
                  board[drow][dcol]=nextLetter
                  # place the letter and hope it works
                  solution=solve(board,nextLetter,drow, dcol)
                  if(solution!=None):
                     return solution
                  #undo prior step
                  board[drow][dcol]="-"
         # shoot, can't place the letter
         return None
      
   return solve(board,"A",aLocation[0],aLocation[1])      
         
#MickeyMouse!
import math
from Tkinter import *

def mousePressed(canvas,event):
    canvas.data.mouseText = "last mousePressed: " + str((event.x, event.y))
    redrawAll(canvas)

def keyPressed(canvas,event):
    if (event.keysym in ["Up", "Right"]):
        canvas.data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (canvas.data.level > 0)):
        canvas.data.level -= 1
    redrawAll(canvas)

def timerFired(canvas):
    canvas.data.timerCounter += 1
    canvas.data.timerText = "timerCounter = " + str(canvas.data.timerCounter)
    redrawAll(canvas)
    delay = 250 # milliseconds
    def f():
       timerFired(canvas)
    canvas.after(delay, f)
    
def mickeyFace(canvas, xc, yc, r):
    eyex=xc
    eyey=yc-r/8
    nosex=xc
    nosey=yc+r/3
    eyeWidth=r/8
    eyeHeight=r/3
    noseW=r/5
    noseHeight=eyeWidth
    #create white face! circle    
    canvas.create_oval(xc-r,yc-r,xc+r,yc+r,fill="white")
    canvas.create_oval(nosex-noseW,nosey-noseHeight,nosex+noseW,nosey+
                       noseHeight, fill="black")
    eyeSpace=r/4
    #left eye
    canvas.create_oval(eyex-eyeWidth-eyeSpace,eyey-eyeHeight,
                       eyex+eyeWidth-eyeSpace,eyey+eyeHeight,fill="black")
    #right eye
    canvas.create_oval(eyex-eyeWidth+eyeSpace,eyey-eyeHeight,
                       eyex+eyeWidth+eyeSpace,eyey+eyeHeight,fill="black")
    #make smile!
    arcRadius=2*r/3
    canvas.create_arc(xc-arcRadius,yc-arcRadius,xc+arcRadius,
                      yc+arcRadius,start=210,extent=110,style=ARC)    
    
def fractalMickeyMouse(canvas, xc, yc, r, level):
    mickeyFace(canvas, xc, yc, r)
    if(level==0):return
    else:
       newR=r/2
       shift=(3*r/2)/ math.sqrt(2)
       #left ear
       fractalMickeyMouse(canvas, xc-shift, yc-shift, newR, level-1)
       #right ear
       fractalMickeyMouse(canvas, xc+shift, yc-shift, newR, level-1)
       
def redrawAll(canvas):
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,460,400,fill="green")
    xc=240
    yc=300
    r=100
    level=6
    fractalMickeyMouse(canvas, xc, yc, r, canvas.data.level)
    # draw the text
    canvas.create_text(200, 25,
                       text = "Level %d Mickey Mouse" % (canvas.data.level),
                       font = "Arial 26 bold")
    canvas.create_text(200, 50,
                       text = "Use arrows to change level",
                       font = "Arial 10")

def init(canvas):
    canvas.data.level=0
    canvas.data.mouseText = "No mousePresses yet"
    canvas.data.keyText = "No keyPresses yet"
    canvas.data.timerText = "No timerFired calls yet"
    canvas.data.timerCounter = 0

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=460, height=400)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init(canvas)
    # set up events
    def f(event):mousePressed(canvas,event)
    root.bind("<Button-1>", f)
    root.bind("<Key>", lambda event: keyPressed(canvas,event))
    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
      
   
######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################
def testLargestFile():
   assert(findLargestFile("sampleFiles/folderA") ==
                       "sampleFiles/folderA/folderC/giftwrap.txt")
   assert(findLargestFile("sampleFiles/folderB") ==
                          "sampleFiles/folderB/folderH/driving.txt")
   assert(findLargestFile("sampleFiles/folderB/folderF") == "")
   print "passed LargestFile"

def testFlatten():
   #print "hi"
   assert(flatten([1,[2]]) == [1,2])
   #print "hi2"
   assert(flatten([1,2,[3,[4,5],6],7]) == [1,2,3,4,5,6,7])
   #print "hi3"
   assert(flatten(['wow', [2,[[]]], [True]]) ==['wow', 2, True])
   #print "hi4"
   assert(flatten([]) ==[])
   assert(flatten([[]]) ==[])
   assert(flatten(3) == 3)

   print "passed Flatten"
   
def testSolveABC():
    print "Testing solveABC()...",
    constraints = "CHJXBOVLFNURGPEKWTSQDYMI"
    aLocation = (0,4)
    board = solveABC(constraints, aLocation)
    solution = [['I', 'J', 'K', 'L', 'A'],
                ['H', 'G', 'F', 'B', 'M'],
                ['T', 'Y', 'C', 'E', 'N'],
                ['U', 'S', 'X', 'D', 'O'],
                ['V', 'W', 'R', 'Q', 'P']
               ]
    assert(board == solution)
    print "Passed!" 

def testAll():
    testSolveABC()
    testFlatten()
    testLargestFile()

testAll()

