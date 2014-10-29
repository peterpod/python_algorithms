# sierpinsky-triangle.py

from Tkinter import *

def drawSierpinskyTriangle(canvas, x, y, size, level):
    # (x,y) is the lower-left corner of the triangle
    # size is the length of a side
    x = float(x)
    y = float(y)
    if (level == 0):
        canvas.create_polygon(x, y,
                              x+size, y,
                              x+size/2, y-size*(3**0.5)/2,
                              fill="black")
    else:
        drawSierpinskyTriangle(canvas, x, y, size/2, level-1)
        drawSierpinskyTriangle(canvas, x+size/2, y, size/2, level-1)
        drawSierpinskyTriangle(canvas, x+size/4, y-size*(3**0.5)/4, size/2, level-1)

def keyPressed(event):
    if (event.keysym in ["Up", "Right"]):
        canvas.data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (canvas.data.level > 0)):
        canvas.data.level -= 1
    redrawAll()

def redrawAll():
    canvas.delete(ALL)
    drawSierpinskyTriangle(canvas, 25, 450, 450, canvas.data.level)
    canvas.create_text(250, 25,
                       text = "Level %d Sierpinsky Triangle" % (canvas.data.level),
                       font = "Arial 26 bold")
    canvas.create_text(250, 50,
                       text = "Use arrows to change level",
                       font = "Arial 10")

def init():
    canvas.data.level = 1
    redrawAll()

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root, width=500, height=500)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init()
    # set up events
    #root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    #timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
