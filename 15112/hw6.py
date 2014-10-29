#hw4.py
# Peter Podniesinski + ppodnies + H

"""
hwb Reasoning over code
f1.
#answer: x=8 y=2.
#you start the problem off by seeing x+y==10
#therefore x is between (6,8) and y can be between (2,4)
#since x>y. Then you look at the bit wise function assert.
#So you should test the possibilities. 8,2 works because
#8<<2 is 32 and 32>>2 is simply 8

f2.
#answer x=31 y=13
#in this function x>y and x+y ==44 therefore
#you can determine that x must be larger that 22
# and y can be anything less than 22. Next, you figure out
#that x%y==5 so you must choose two numbers that satisfy this
#by checking numbers after 22 you find 31, 13 work. so
#31+13 ==44 and 31 mod 13==5. This also satisfies
#13==31%10*10 + x/10 since this = 1*10 +3=13

f3.
#answer: x=67 y=1
#in this function you can determine that y cannot equal
#2 because any x >10 will already make a sumation larger than 100.
#for example 10**2==100. That means that y must equal 1. x=67 will
# satisfy the boolen restraints because 67/2=33 +67==100

f4.
#anwer: x=32 y=8
#this is because x+y==40 and x>y. The hard part
# was to satisfy the bitwise or operation. so
#(x|y == 40) Basically this will demostrate the or operation
#for binary. 32 is 100000 because binary works by 2*n and
#8 is 1000. Therefore x bitwise or y will go through the binary
#and decide if there is a the index satisfies the or which is only
#false when both are 0. Since 100000+1000=101000 you just add the two

f6.
#answer f6(18)
#First off you know that 100>x>1 next you figure out
#that y=x originally and ends up as 21 so x should be <21
#but not too small. You also know that by going through
#the loop y increments if z%7==0. If you pick 18 then y
#will increment 3 times at z=0,7,14

f9.
#answer:31
#First, you see that 100>x>10
#Next, you see that z multiplys each time by 2.
#so possible z values are 2,4,8,16,32. and one of
#these values is 1 greater than x. Next you must
#look at these numbers and figure out what x/6 equals.
#because this will be the number of times y increments.
#x=31 will work because z*2 will happen 6 times making
#z=32. then y==31/6= 5 this value works because y will
#increment 5 times accoring to the while condition z<x


"""

######################################################################
# Place your non-graphics solutions here!
######################################################################
import random
import math
import string

def convertToNumber(s,solution):
   number=0
   for index in xrange(len(s)):
      for digits in xrange(len(solution)):
         if(s[index]==solution[digits]):
            #if index in s1== index in puzzle
            #add the index to digits to start converting
            number*=10
            number+=digits
            #multiply to shift total over one place holder
   return number

#print convertToNumber("MONEY","OMY--ENDRS")

def solvesCryptarithm(puzzle, solution):
   (s1,s2,s3)=(puzzle[:puzzle.find("+")],puzzle[puzzle.find("+")+1:puzzle.find("=")],
            puzzle[puzzle.find("=")+1:len(puzzle)])
   #this splits the puzzle into 3 different string
   number1=convertToNumber(s1,solution)
   number2=convertToNumber(s2,solution)
   number3=convertToNumber(s3,solution)
   #if the sum of converted numbers=number3 we have a correct
   #solution.
   if(number1+number2==number3):
      return True
   else:
      return False

#print solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS")

import copy
def findWords(dictionary,hand):
   word=""
   copyHand=copy.copy(hand)
   possibleWords=[]
   i=0
   charUseCount=0
   charRepeatCount=[0]*len(hand)
   for i in xrange(len(dictionary)):
      for j in xrange(len(dictionary[i])):
         for k in xrange(len(hand)):
            #create possible hands by reaarranging char's in list hand
            if ((dictionary[i][j]==hand[k])and charRepeatCount[k]==0
                and charUseCount==0):
               #charRepeatCount makes sure the same character is not
               #used more than once
               print word
               word+=hand[k]
               charRepeatCount[k]+=1
               charUseCount+=1
         charUseCount=0
      #for every word in dictionary reset charRepeatCount
      if (word==dictionary[i]):
               #if the word == word in dictionary at end of loop
               #add word to possible Words.
         possibleWords+=[word]
      charRepeatCount=[0]*len(hand)
      word=""
   if(len(possibleWords)==0):
      return None
   else:
      return possibleWords

print findWords(['xyz', 'zxy', 'zzy', 'yy', 'yx', 'wow'], ['x', 'y', 'z', 'y'])

def score(letterScores,hand):
   score=0
   alphabet = string.ascii_lowercase
   #finds the possible words that can be made from the hand.
   if(hand==None):
      return 0
   for i in xrange(len(hand)):
      for j in xrange(len(hand[i])):
         for k in xrange(len(letterScores)):
            if(hand[i][j]==alphabet[k]):
               #if the character is the same char in alphabet
               #add the value from letterscore to score since alphabet
               #and letterscore is same length
               score+=letterScores[k]
   return score
   
#print score([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5,
 #            1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1], ['x', 'y', 'z'])


def bestScrabbleScore(dictionary, letterScores,hand):
   bestScrabbleScore=[]
   bestScore=0
   possibleMoves=findWords(dictionary,hand)
   if(possibleMoves==None):
      return None
   print possibleMoves
   for index in xrange(len(possibleMoves)):
      if(score(letterScores,possibleMoves[index])>=bestScore):
         #compares bestscore so far, finds the index
         #print bestScore, bestScrabbleScore
         bestScore=score(letterScores,possibleMoves[index])
         bestScrabbleScore+=[possibleMoves[index]]
   if(len(bestScrabbleScore)==1):
      return bestScrabbleScore[0], bestScore
   else:
      return bestScrabbleScore, bestScore

print bestScrabbleScore(['xyz', 'zxy', 'zzy', 'yy', 'yx', 'wow'],
                        [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5,
                         1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1], ['w', 'x', 'z'])

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################
# Othello case study
import random

def make2dList(rows, cols):
    a=[]
    for row in xrange(rows): a += [[0]*cols]
    return a

def hasMove(board, player):
    (rows, cols) = (len(board), len(board[0]))
    for row in xrange(rows):
        for col in xrange(cols):
            if (hasMoveFromCell(board, player, row, col)):
                return True
    return False

def hasMoveFromCell(board, player, startRow, startCol):
    (rows, cols) = (len(board), len(board[0]))
    if (board[startRow][startCol] != 0):
        return False
    for dir in xrange(8):
        if (hasMoveFromCellInDirection(board, player, startRow, startCol, dir)):
            return True
    return False

def hasMoveFromCellInDirection(board, player, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]
    i = 1
    while True:
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)):
            return False
        elif (board[row][col] == 0):
            # no blanks allowed in a sandwich!
            return False
        elif (board[row][col] == player):
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich
            i += 1
    return (i > 1)

def makeMove(board, player, startRow, startCol):
    # assumes the player has a legal move from this cell
    (rows, cols) = (len(board), len(board[0]))
    for dir in xrange(8):
        if (hasMoveFromCellInDirection(board, player, startRow, startCol, dir)):
            makeMoveInDirection(board, player, startRow, startCol, dir)
    board[startRow][startCol] = player

def makeMoveInDirection(board, player, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]
    i = 1
    while True:
        row = startRow + i*drow
        col = startCol + i*dcol
        if (board[row][col] == player):
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich, so flip it!
            board[row][col] = player
            i += 1

def getPlayerLabel(player):
    labels = ["-", "X", "O","."]
    return labels[player]

def printColLabels(board):
    (rows, cols) = (len(board), len(board[0]))
    print "  ", # skip row label
    for col in xrange(cols): print chr(ord("A")+col),
    print

def printBoard(board,player):
    (rows, cols) = (len(board), len(board[0]))
    printColLabels(board)
    for row in xrange(rows):
        print "%2d" % (row+1),
        for col in xrange(cols):
            if(not isLegalMove(board,player,row,col)):
                print getPlayerLabel(board[row][col]),
            else:
                print ".",
        print "%2d" % (row+1)
    printColLabels(board)

def isLegalMove(board, player, row, col):
    (rows, cols) = (len(board), len(board[0]))
    if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)): return False
    return hasMoveFromCell(board, player, row, col)

def getMove(board, player):
    print "\n**************************"
    printBoard(board,player)
    row=len(board)
    col=len(board)
    while True:
        if(getPlayerLabel(player)!="X"):
           rows=random.randrange(1,row+1)
           cols=random.randrange(1,col+1)
           while isLegalMove(board,player,rows,cols)!=True:
              rows=random.randrange(1,row+1)
              cols=random.randrange(1,col+1)
           return (rows,cols)
        prompt = "Enter move for player " + getPlayerLabel(player) + ": "
        move = raw_input(prompt).upper()
        # move is something like "A3"
        if ((len(move) < 2) or (not move[0].isalpha()) or (not move[1].isdigit())):
            print "Wrong format!  Enter something like A3 or D5."
        else:
            col = ord(move[0]) - ord('A')
            #fix condition for boards larger than 9
            row = int(move[1:])-1
            if (not isLegalMove(board, player, row, col)):
                print "That is not a legal move!  Try again."
            else:
                return (row, col)

def getLegalMoves(board,player):
    legalMoves=[]
    for rows in xrange(len(board)):
        for cols in xrange(len(board[row])):
            if(isLegalMove(board,player,rows,cols)):
                legalMoves+=[(rows,cols)]
    return LegalMoves

def score(board,player,score):
    for row in range(len(board)):
        for col in range(len(board)):
            if(board[row][col]==player):
                score+=1
    return score

def playOthelloAgainstRandomComputer(rows,cols):
    # create initial board
    board = make2dList(rows, cols)
    board[rows/2][cols/2] = board[rows/2-1][cols/2-1] = 1
    board[rows/2-1][cols/2] = board[rows/2][cols/2-1] = 2
    (currentPlayer, Computer) = (1, 2)
    scoreCurrentPlayer,scoreOtherPlayer=(0,0)
    # and play until the game is over
    while True:
        if (hasMove(board, currentPlayer) == False):
            if (hasMove(board, Computer)):
                print "No legal move!  PASS!"
                (currentPlayer, Computer) = (Computer, currentPlayer)
            else:
                print "No more legal moves for either player!  Game over!"
                break
        print "Score:", score(board,currentPlayer,scoreCurrentPlayer), "," ,
        print score(board,Computer,scoreOtherPlayer)
        (row, col) = getMove(board, currentPlayer)
        makeMove(board, currentPlayer, row, col)
        (currentPlayer, Computer) = (Computer, currentPlayer)
    print "Goodbye!"

#playOthelloAgainstRandomComputer(8,8)

def playOthello(rows, cols):
    # create initial board
    board = make2dList(rows, cols)
    board[rows/2][cols/2] = board[rows/2-1][cols/2-1] = 1
    board[rows/2-1][cols/2] = board[rows/2][cols/2-1] = 2
    (currentPlayer, otherPlayer) = (1, 2)
    scoreCurrentPlayer,scoreOtherPlayer=(0,0)
    # and play until the game is over
    while True:
        if (hasMove(board, currentPlayer) == False):
            if (hasMove(board, otherPlayer)):
                print "No legal move!  PASS!"
                (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)
            else:
                print "No more legal moves for either player!  Game over!"
                break
        print "Score:", score(board,currentPlayer,scoreCurrentPlayer), "," ,
        print score(board,otherPlayer,scoreOtherPlayer)
        (row, col) = getMove(board, currentPlayer)
        makeMove(board, currentPlayer, row, col)
        (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)
    print "Goodbye!"

#playOthello(8,8)

#start of Memory Game
import time
import math

def make2dList(rows,cols):
   a=[]
   for row in xrange(rows): a += [[0]*cols]
   return a

def getPlayerLabel(player):
    labels = ["$", "X", "O"]
    return labels[player]
   
def printColLabels(board):
    (rows, cols) = (len(board), len(board[0]))
    print "  ", # skip row label
    for col in xrange(cols): print chr(ord("A")+col),
    print

def printBoard(board,hidden):
    (rows, cols) = (len(board), len(board[0]))
    printColLabels(board)
    for row in xrange(rows):
        print "%2d" % (row+1),
        for col in xrange(cols):
            if(board[row][col]!=0):
               print hidden[row][col],
            else:               
               print getPlayerLabel(board[row][col]),
        print "%2d" % (row+1)
    printColLabels(board)

def spacesHidden(board):
   spacesHidden=0
   for row in range(len(board)):
      for col in range(len(board)):
         #print board[row][col]
         if(board[row][col]!=0):
            pass
         else:
            spacesHidden+=1
   return spacesHidden

def isLegalMove(board,row1, col1, row2,col2):
    (rows, cols) = (len(board), len(board[0]))
    if ((row1 < 0) or (row1 >= rows) or (row2<0) or(row2>=rows) or (col1 < 0) or (col1 >= cols)
        or (col2<0) or(col2>=cols)):
       return False
    return True

def getMove(board,hidden,score):
   print "\n**************************"
   printBoard(board,hidden)
   prompt= "Enter your guess:"
   move=raw_input(prompt).upper()
   if ((len(move)<7)or((move[1].isalpha() and move[4].isalpha())!=True)
       or ((move[2].isdigit() and move[5].isdigit()) !=True)):
      print "Wrong format!  Enter something like (A3,D5)"
   else:
      col1 = ord(move[1]) - ord('A')
      row1 = int(move[2:move.find(",")])-1
      col2 = ord(move[4]) - ord('A')
      row2 = int(move[5:move.find(")")])-1
      if (not isLegalMove(board, row1, col1,row2,col2)):
         print "That is not a legal move!  Try again."
      else:
         return makeMove(board,hidden, row1, col1, row2,col2,score)

def makeMove(board,hidden,row1,col1,row2,col2,score):
   #check if hidden numbers are the same
   rows=len(board)
   cols=len(board[0])
   #hidden=hiddenNumbers(rows,cols)
   if(hidden[row1][col1]==hidden[row2][col2]):
      board[row1][col1]=hidden[row1][col1]
      board[row2][col2]=hidden[row2][col2]
      print "You guessed right!"
      
   else:
      print "Try another guess"
      board[row1][col1]=hidden[row1][col1]
      board[row2][col2]=hidden[row2][col2]
      printBoard(board,hidden)
      board[row1][col1]=0
      board[row2][col2]=0
      score+=1
   #print board, hidden

def hiddenNumbers(rows,cols):
   #this function encodes the numbers from 1 to RC
   #into an array a random amount exactly 2 times
   hiddenNumbers=make2dList(rows,cols)
   maxNumber=(rows*cols)/2
   randomNumberCount=[0]*maxNumber
   #print maxNumber, len(randomNumberCount)
   for row in xrange(rows):
      for col in xrange(cols):
         randomNumber=random.randrange(1,maxNumber+1)
         #range 1,R*C
         while randomNumberCount[randomNumber-1]>=2:
            #subtract 1 to avoid index out of range
            #makes sure you choose a number no more than twice.
            randomNumber=random.randrange(1,maxNumber+1)
         else:
            hiddenNumbers[row][col]=randomNumber
            randomNumberCount[randomNumber-1]+=1
   return hiddenNumbers

def playMemoryGame(rows,cols):
   board=make2dList(rows,cols)
   #printBoard(board)
   hidden=hiddenNumbers(rows,cols)
   score=0
   startTime=time.time()
   while spacesHidden(board)!=0:
         getMove(board,hidden,score)
   printBoard(board,hidden)
   endTime=time.time()
   return "Your score is:", score, "Your time is:", round(endTime-startTime),"seconds!"
   #return 42

#print playMemoryGame(2,2)
   
######################################################################
# Place your (optional) additional tests here
######################################################################

import sys
from cStringIO import StringIO

def consoleFreeCall(fn, args, inputStrings=[]):
    outputStrings = "<failed to capture console output>"
    originalOut = sys.stdout
    global raw_input
    originalRawInput = raw_input
    try:
        sys.stdout = StringIO()
        if (inputStrings != []):
            def newRawInput(prompt=""): return inputStrings.pop(0)
            raw_input = newRawInput
        fn(*args)
        outputStrings = sys.stdout.getvalue()
        sys.stdout.close()
    finally:
        sys.stdout = originalOut
        raw_input = originalRawInput
        return outputStrings

def g(x):
    while True:
        y = int(raw_input("Enter y (0 when done): "))
        if (y == 0): break
        print "%d*%d is %d" % (x, y, x*y)

def runConsoleFreeTests():
    print "running console-free tests...",
    assert(consoleFreeCall(f, [42]) == "2*42 is 84\n")
    assert(consoleFreeCall(g, [2], ["3", "4", "0"]) == "2*3 is 6\n2*4 is 8\n")
    print "passed!"

#runConsoleFreeTests()

def runMoreStudentTests():
    print "Running additional tests...",
    
def testBestScrabbleScore():
    print "testing.. " ,
    assert(bestScrabbleScore(["hi","hey","hello"],[
   #  a, b, c, d, e, f, g, h, i, j, k, l, m
      1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
   #  n, o, p, q, r, s, t, u, v, w, x, y, z
      1, 1, 3,10, 1, 1, 1, 1, 4, 4, 8, 4,10], [
         "h","y","e","l","i","l","o"]) == ["hello"],14)
    print "passed BestScrabbleScore "
    
def testSolvesCryptarithm():
    print "testing.. ",
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS")==True)
    assert(solvesCryptarithm("SEND+MARE=MONEY","OMY--ENDRS")==False)
    assert(solvesCryptarithm("SzND+ARE=MONEY","OSY--EZDRW")==False)
    print "passed..SolvesCryptarithm "

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
    #testBestScrabbleScore()
    #testSolvesCryptarithm()

if __name__ == "__main__":
    main()

