def solveABC(constraints,aLocation):
   board=[]
   d=dict()
   boardRow=len(constraints)
   row=5
   col=5
   for rows in range(row):board+=[["-"]*col]
   board[aLocation[0]][aLocation[1]]="A"
   #set up constraints in a dictionary
   #each row/col should have5 values..corners
   #are edge cases
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
   #print toprowString,bottomrowString,topcolString,bottomcolString
   for index in xrange(row):
      #print index,row-index
      colList+=[(toprowString[index],bottomrowString[row-index-1])]
   for index in xrange(row):
      rowList+=[(topcolString[index],bottomcolString[row-index-1] )]
   #print toprowString,bottomrowString,topcolString,bottomcolString
   #print rowList
   #print colList  
   def isLegal(letter,previous, row, col):
        # a position is legal if it's on the board and
        #if it follows the constraints array and is, adjacent
        #to a prior letter
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
           print "its diagonal"
           if(letter==diagonalListRight[0][0] or letter==diagonalListRight[0][1]):
              return True
        elif(row+col==4):
           if(letter==diagonalListLeft[0][0] or letter==diagonalListLeft[0][1]):
              return True
        return False        
        
   def solved(board):
      for row in xrange(len(board)):
         for col in xrange(len(board[0])):
            if(board[row][col]=="-"):
               return False
      return True
   
   def solve(board,letter, row, col):
      nextLetter=chr(ord(letter)+1)
      print board
      if(solved(board)==True):
         #finished the puzzle, return board assuming
         #it has all the correct values
         return board
      else:
         for rows in xrange(-1,2):
            for cols in xrange(-1,2):
               drow=row+rows
               dcol=col+cols
               #print isLegal(nextLetter,letter,drow,dcol)
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
         
 
######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################   
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

testSolveABC()
