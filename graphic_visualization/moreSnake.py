#snake.py

import random
from Tkinter import *

def mousePressed(canvas,event):
    margin=canvas.data.margin
    cellSize=canvas.data.cellSize
    snakeBoard=canvas.data.snakeBoard
    if(canvas.data.isPaused):
       cx=(event.y-margin)/cellSize
       cy=(event.x-margin)/cellSize
       newWallCenter = (cx,cy)
       canvas.data.wallCenter.append(newWallCenter)
       snakeBoard[cx][cy]=-3
       #create wall
       canvas.data.wallPlacedTime=canvas.data.score  
    redrawAll(canvas)

def keyPressed(canvas,event):
    canvas.data.ignoreNextTimerEvent = True # for better timing
    # first process keys that work even if the game is over
    if (event.char == "q"):
        gameOver(canvas)
    elif (event.char == "r"):
        init(canvas)
    elif (event.char == "d"):
        canvas.data.inDebugMode = not canvas.data.inDebugMode
    elif (event.char == "p"):
        canvas.data.isPaused= not canvas.data.isPaused
    # now process keys that only work if the game is not over
    if (canvas.data.isGameOver == False):
        if (event.keysym == "Up"):
            moveSnake(canvas,-1, 0)
        elif (event.keysym == "Down"):
            moveSnake(canvas,+1, 0)
        elif (event.keysym == "Left"):
            moveSnake(canvas,0,-1)
        elif (event.keysym == "Right"):
            moveSnake(canvas,0,+1)
    redrawAll(canvas)

def moveSnake(canvas,drow, dcol):
    if(canvas.data.isPaused==True):
       pass
    else:
       # move the snake one step forward in the given direction.
       canvas.data.snakeDrow = drow # store direction for next timer event
       canvas.data.snakeDcol = dcol
       snakeBoard = canvas.data.snakeBoard
       rows = len(snakeBoard)
       cols = len(snakeBoard[0])
       headRow = canvas.data.headRow
       headCol = canvas.data.headCol
       newHeadRow = headRow + drow
       newHeadCol = headCol + dcol
       score=canvas.data.score
       if ((newHeadRow < 0) or (newHeadRow >= rows) or
           (newHeadCol < 0) or (newHeadCol >= cols)):
           # snake ran off the board
           canvas.data.highestScore+=[canvas.data.score]
           gameOver(canvas)
       elif (snakeBoard[newHeadRow][newHeadCol] > 0):
           # snake ran into itself!
           canvas.data.highestScore+=[canvas.data.score]
           gameOver(canvas)
       elif (snakeBoard[newHeadRow][newHeadCol] == -1):
           # eating food!  Yum!
           snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol];
           canvas.data.headRow = newHeadRow
           canvas.data.headCol = newHeadCol
           score+=1
           canvas.data.score=score
           placeFood(canvas)
       elif(snakeBoard[newHeadRow][newHeadCol]==-2):
           gameOver(canvas)
       elif(snakeBoard[newHeadRow][newHeadCol]==-3):
           snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol];
           canvas.data.headRow = newHeadRow
           canvas.data.headCol = newHeadCol
           removeTail(canvas)
           score-=1
           canvas.data.score=score
       else:
           # normal move forward (not eating food)
           snakeBoard[newHeadRow][newHeadCol] = 1 + snakeBoard[headRow][headCol];
           canvas.data.headRow = newHeadRow
           canvas.data.headCol = newHeadCol
           removeTail(canvas)

def removeTail(canvas):
    # find every snake cell and subtract 1 from it.  When we're done,
    # the old tail (which was 1) will become 0, so will not be part of the snake.
    # So the snake shrinks by 1 value, the tail.
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > 0):
                snakeBoard[row][col] -= 1

def gameOver(canvas):
    canvas.data.isGameOver = True

def doTimerFired(canvas):
    redrawAll(canvas)

def timerFired(canvas):
    if( canvas.data.isPaused==False):
       doTimerFired(canvas)
    ignoreThisTimerEvent = canvas.data.ignoreNextTimerEvent
    canvas.data.ignoreNextTimerEvent = False
    if ((canvas.data.isGameOver == False) and
        (ignoreThisTimerEvent == False)):
        # only process timerFired if game is not over
        drow = canvas.data.snakeDrow
        dcol = canvas.data.snakeDcol
        moveSnake(canvas,drow, dcol)
        redrawAll(canvas)
    # whether or not game is over, call next timerFired
    # (or we'll never call timerFired again!)
    if(canvas.data.score>=4):
       #Speeds up!
       delay=90
    else:
       delay = 150 # milliseconds
    def f():
       timerFired(canvas)
    canvas.after(delay, f) # pause, then call timerFired again

def numWalls(canvas):
   snakeBoard=canvas.data.snakeBoard
   rows = len(snakeBoard)
   cols = len(snakeBoard[0])
   numWalls=0
   for row in range(rows):
       for col in range(cols):
           if (snakeBoard[row][col] == -3):
               numWalls+=1

   return numWalls
   

def redrawAll(canvas):
    canvas.delete(ALL)
    score=canvas.data.score
    scoreMargin=canvas.data.scoreMargin
    margin=canvas.data.margin
    cx = canvas.data.canvasWidth/2
    highestScore=canvas.data.highestScore
    drawSnakeBoard(canvas)
    cellSize=canvas.data.cellSize
    for wallCenter in canvas.data.wallCenter:
       (row,col)=wallCenter
       left = margin + col * cellSize
       right = left + cellSize
       top = scoreMargin+margin + row * cellSize
       bottom = top + cellSize       
       canvas.create_rectangle(left,top,right,bottom,fill="brown")
    if(canvas.data.score<0):
       gameOver(canvas)
    if (canvas.data.isGameOver == True):
        bonus=0
        if((canvas.data.score-canvas.data.wallPlacedTime)>10): 
           bonus=20*numWalls(canvas)
        score=score+bonus
        cx = canvas.data.canvasWidth/2
        cy = canvas.data.canvasHeight/2
        cy1=cy+canvas.data.canvasHeight/4
        canvas.create_text(cx, cy, text="Game Over!", font=("Helvetica", 32, "bold"))
        canvas.create_text(cx, cy1, text="HighestScoreList:", font=("Helvetica", 16, "bold"))
        canvas.create_text(cx+cellSize*4.6, cy1, text=highestScore, font=("Helvetica", 18, "bold"))
    canvas.create_text(cx, scoreMargin/2,text="Score:",font=("Helvetica",12))
    canvas.create_text(cx+cellSize+margin, scoreMargin/2,text=score,font=("Helvetica",12))
   
def drawSnakeBoard(canvas):
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    for row in range(rows):
        for col in range(cols):
            drawSnakeCell(canvas,snakeBoard, row, col)

def drawSnakeCell(canvas,snakeBoard, row, col):
    scoreMargin=canvas.data.scoreMargin
    margin = canvas.data.margin
    cellSize = canvas.data.cellSize
    left = margin + col * cellSize
    right = left + cellSize
    top = scoreMargin+margin + row * cellSize
    bottom = top + cellSize
    gridColor="white"
    snakeColor="blue"
    foodColor="green"
    poisonColor="red"
    if canvas.data.isPaused :
       #make screen dimmer
       gridColor="#C0C0C0"
       snakeColor="#008080"
       poisonColor="brown"
       foodColor="#808000"
    canvas.create_rectangle(left, top, right, bottom, fill=gridColor)
    if (snakeBoard[row][col] > 0):
        # draw part of the snake body
        canvas.create_oval(left, top, right, bottom, fill=snakeColor)
    elif (snakeBoard[row][col] ==-1):
        # draw food
        canvas.create_oval(left, top, right, bottom, fill=foodColor)
    elif (snakeBoard[row][col] ==-2):
        # draw food
        canvas.create_oval(left, top, right, bottom, fill=poisonColor)
    # for debugging, draw the number in the cell
    if (canvas.data.inDebugMode == True):
        canvas.create_text(left+cellSize/2,top+cellSize/2,
                           text=str(snakeBoard[row][col]),font=("Helvatica", 14, "bold"))

def loadSnakeBoard(canvas):
    rows = canvas.data.rows
    cols = canvas.data.cols
    snakeBoard = [ ]
    for row in range(rows): snakeBoard += [[0] * cols]
    snakeBoard[rows/2][cols/2] = 1
    canvas.data.snakeBoard = snakeBoard
    findSnakeHead(canvas)
    placeFood(canvas)

def placeFood(canvas):
    # place food (-1) in a random location on the snakeBoard, but
    # keep picking random locations until we find one that is not
    # part of the snake!
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    while True:
        row = random.randint(0,rows-1)
        col = random.randint(0,cols-1)
        if (snakeBoard[row][col] == 0 or snakeBoard[row][col]==-2
        or snakeBoard[row][col]==-3):
            break
    snakeBoard[row][col] = -1

def placePoison(canvas):
    snakeBoard=canvas.data.snakeBoard
    cols=len(snakeBoard[0])
    rows=len(snakeBoard)
    headRow=canvas.data.headRow
    headCol=canvas.data.headCol
    while True:
       #place poison
       row = random.randint(0,rows-1)
       col = random.randint(0,cols-1)
       if (snakeBoard[row][col]==0 or snakeBoard[row][col]==-1
       or snakeBoard[row][col]==-3):
          break
       #check if its 1 place away from head
       elif((abs(headRow-row)<=1)and (abs(headCol-col)<=1)):
          break
    snakeBoard[row][col]=-2
                  

def findSnakeHead(canvas):
    # find where snakeBoard[row][col] is largest, and
    # store this location in headRow, headCol
    snakeBoard = canvas.data.snakeBoard
    rows = len(snakeBoard)
    cols = len(snakeBoard[0])
    headRow = 0
    headCol = 0
    for row in range(rows):
        for col in range(cols):
            if (snakeBoard[row][col] > snakeBoard[headRow][headCol]):
                headRow = row
                headCol = col
    canvas.data.headRow = headRow
    canvas.data.headCol = headCol

def printInstructions():
    print "Snake!"
    print "Use the arrow keys to move the snake."
    print "Eat food to grow."
    print "Stay on the board!"
    print "And don't crash into yourself!"
    print "Press 'd' for debug mode."
    print "Press 'r' to restart."

def init(canvas):
    printInstructions()
    loadSnakeBoard(canvas)
    highestScore=[]
    canvas.data.inDebugMode = False
    canvas.data.isGameOver = False
    canvas.data.snakeDrow = 0
    canvas.data.snakeDcol = -1 # start moving left
    canvas.data.ignoreNextTimerEvent = False
    canvas.data.isPaused=False
    canvas.data.wallPlacedTime=0
    canvas.data.score=1
    canvas.data.highestScore=highestScore
    canvas.data.wallCenter=[]
    placePoison(canvas)
    redrawAll(canvas)

########### copy-paste below here ###########

def run(rows, cols):
    # create the root and the canvas
    root = Tk()
    scoreMargin=20
    margin = 5
    cellSize = 30
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize+scoreMargin
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.scoreMargin=scoreMargin
    canvas.data.margin = margin
    canvas.data.cellSize = cellSize
    canvas.data.canvasWidth = canvasWidth
    canvas.data.canvasHeight = canvasHeight
    canvas.data.rows = rows
    canvas.data.cols = cols
    init(canvas)
    # set up events
    def f(event):mousePressed(canvas,event)
    root.bind("<Button-1>", f)
    root.bind("<Key>", lambda event: keyPressed(canvas,event))
    timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run(20,20)
