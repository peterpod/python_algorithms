# wordSearch.py
# This code was developed in class on Tue 4-Oct-2011.
# As such, it may not contain perfect style, and may
# even contain a small bug here or there (usual disclaimer).

def wordSearch(puzzle, word):
    rows = len(puzzle)
    cols = len(puzzle[0])
    for startRow in xrange(rows):
        for startCol in xrange(cols):
            solution = wordSearch1(puzzle, word, startRow, startCol)
            if (solution != None):
                return solution
    return None

def wordSearch1(puzzle, word, startRow, startCol):
    rows = len(puzzle)
    cols = len(puzzle[0])
    for drow in xrange(-1,2):
        for dcol in xrange(-1, 2):
            if ((drow != 0) or (dcol != 0)):
                solution = wordSearch2(puzzle, word, startRow, startCol, drow, dcol)
                if (solution != None):
                    return solution
    return None

def wordSearch2(puzzle, word, startRow, startCol, drow, dcol):
    rows = len(puzzle)
    cols = len(puzzle[0])
    for i in xrange(len(word)):
        cWord = word[i]
        puzzleRow = startRow+i*drow
        puzzleCol = startCol+i*dcol
        if ((puzzleRow < 0) or (puzzleRow >= rows) or
            (puzzleCol < 0) or (puzzleCol >= cols)):
            return None
        cPuzzle = puzzle[puzzleRow][puzzleCol]
        if (cWord != cPuzzle):
            return None
    # found it!
    return (startRow, startCol, (drow, dcol))

def printPuzzle(puzzle):
    rows = len(puzzle)
    cols = len(puzzle[0])
    for row in range(rows):
        print "   ",
        for col in range(cols):
            print puzzle[row][col],
        print

#############################################

# Now let's try it out!!!!

puzzle = [ [ 'w', 'q', 'r', 'z' ],
           [ 'g', 'o', 'd', 'a' ],
           [ 'w', 'm', 'c', 'c' ]
        ]

print "Here is the puzzle:"
printPuzzle(puzzle)

print "Searching for 'dog':",
print wordSearch(puzzle, "dog")

print "Searching for 'cow':",
print wordSearch(puzzle, "cow")

print "Searching for 'cat':",
print wordSearch(puzzle, "cat")
