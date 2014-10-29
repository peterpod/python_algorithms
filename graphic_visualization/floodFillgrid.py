# FloodFill using Tkinter
# grid-based (not pixel-based), with animation
# and numeric display of depth of recursion
# also, this version is based on our barebones animation code

from Tkinter import *
import time # for time.sleep()

def mousePressed(event, doFlood):
    clearDepths()
    (row,col) = getCell(event.x, event.y)
    if ((row >= 0) and (row < canvas.data.rows) and
        (col >= 0) and (col < canvas.data.cols)):
        color = canvas.data.board[row][col]
        if (color == "cyan"):
            canvas.data.fillColor = "green"
        else:
            canvas.data.fillColor = "cyan"
        if (doFlood):
            floodFillWithLargeStack(row, col)
        else:
            canvas.data.board[row][col] = canvas.data.fillColor

def leftMousePressed(event):
    shiftDown = ((event.state & 0x0001) == 1)
    mousePressed(event, shiftDown)
    redrawAll()

def leftMouseMoved(event):
    (row,col) = getCell(event.x, event.y)
    if ((row >= 0) and (row < canvas.data.rows) and
        (col >= 0) and (col < canvas.data.cols)):
        canvas.data.board[row][col] = canvas.data.fillColor
    redrawAll()

def rightMousePressed(event):
    mousePressed(event, True)
    redrawAll()

def getCell(x, y):
    # return row,col containing the point x,y
    row = (y - 100)/canvas.data.cellSize
    col = x / canvas.data.cellSize
    return (row, col)

def getCellBounds(row, col):
    # return (left, top, right, bottom) of this cell
    left = col * canvas.data.cellSize
    right = (col+1) * canvas.data.cellSize
    top = 100 + row * canvas.data.cellSize
    bottom = 100 + (row+1)*canvas.data.cellSize
    return (left, top, right, bottom) 

def floodFill(row, col, color, depth=0):
    if ((row >= 0) and (row < canvas.data.rows) and
        (col >= 0) and (col < canvas.data.cols) and
        (canvas.data.board[row][col] != color)):
        canvas.data.board[row][col] = color
        canvas.data.depth[row][col] = depth
        redrawAll()
        canvas.update()
        time.sleep(0.05 if (depth < 25) else 0.005)
        floodFill(row-1, col, color, depth+1)
        floodFill(row+1, col, color, depth+1)
        floodFill(row, col-1, color, depth+1)
        floodFill(row, col+1, color, depth+1)

def callWithLargeStack(f,*args):
    import sys
    import threading
    threading.stack_size(2**27)  # 64MB stack
    sys.setrecursionlimit(2**27) # will hit 64MB stack limit first
    # need new thread to get the redefined stack size
    def wrappedFn(resultWrapper): resultWrapper[0] = f(*args)
    resultWrapper = [None]
    #thread = threading.Thread(target=f, args=args)
    thread = threading.Thread(target=wrappedFn, args=[resultWrapper])
    thread.start()
    thread.join()
    return resultWrapper[0]

def floodFillWithLargeStack(row, col):
    callWithLargeStack(floodFill, row, col, canvas.data.fillColor)

def redrawAll():
    canvas.delete(ALL)
    xmid = canvas.data.width/2
    font16b = "Helvetica 16 bold"
    font12i = "Helvetica 12 italic"
    canvas.create_text(xmid,20,text="FloodFill Demo",font=font16b)
    canvas.create_text(xmid,40,text="left click = draw",font=font12i)
    canvas.create_text(xmid,60,text="shift-left or right click = fill",font=font12i)
    canvas.create_text(xmid,80,text="Do not click during floodFill animation!",font=font12i)
    for row in xrange(canvas.data.rows):
        for col in xrange(canvas.data.cols):
            (x0,y0,x1,y1) = bounds = getCellBounds(row, col)
            canvas.create_rectangle(bounds, fill=canvas.data.board[row][col])
            if (canvas.data.depth[row][col] != -1):
                canvas.create_text((x0+x1)/2,(y0+y1)/2,text=str(canvas.data.depth[row][col]))

def clearDepths():
    canvas.data.depth =[([-1]*canvas.data.cols) for row in xrange(canvas.data.rows)]

def init():
    canvas.data.board = [(["cyan"]*canvas.data.cols) for row in xrange(canvas.data.rows)]
    clearDepths()

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    class Struct: pass
    data = Struct()
    data.rows = 4
    data.cols = 6
    data.cellSize = 25 # pixels
    data.width = data.cols * data.cellSize
    data.height = data.rows * data.cellSize + 100 # room for text at top
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.data = data
    canvas.pack()
    init()
    # set up events
    root.bind("<Button-1>", leftMousePressed)
    root.bind("<B1-Motion>",leftMouseMoved)
    root.bind("<Button-3>", rightMousePressed)
    # and launch the app
    redrawAll()
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
