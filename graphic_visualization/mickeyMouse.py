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
    canvas.create_oval(nosex-noseW,nosey-noseHeight,nosex+noseW,nosey+noseHeight,
                       fill="black")
    eyeSpace=r/4
    #left eye
    canvas.create_oval(eyex-eyeWidth-eyeSpace,eyey-eyeHeight,
                       eyex+eyeWidth-eyeSpace,eyey+eyeHeight,fill="black")
    #right eye
    canvas.create_oval(eyex-eyeWidth+eyeSpace,eyey-eyeHeight,
                       eyex+eyeWidth+eyeSpace,eyey+eyeHeight,fill="black")
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
    # draw the text
    xc=240
    yc=300
    r=100
    level=6
    fractalMickeyMouse(canvas, xc, yc, r, canvas.data.level)
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
