# Othello case study

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
    while True:
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
    #print legalMoves
    return LegalMoves

def score(board,player,score):
    for row in range(len(board)):
        for col in range(len(board)):
            if(board[row][col]==player):
                score+=1
    return score                         

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

playOthello(8,8)
