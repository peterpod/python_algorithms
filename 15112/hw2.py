# hw2.py
# name + andrewId + section

"""
   ** Place your manually-graded (Reasoning Over Code) solutions here! **
"""

######################################################################
# Place your non-graphics solutions here!
######################################################################

def sumOfSquaresOfDigits(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit**2
        n=n/10
    return sum

def isHappyNumber(n):
    if(n<1):
        return False
    while n != 1:
        n=sumOfSquaresOfDigits(n) 
        if n==4:
            return False  
    return True      

def nthHappyNumber(n):
    happynumber=1
    count=-1
    while count <=n:
        if(count==n):
            return happynumber
        elif(isHappyNumber(happynumber)==True):
            count+=1
        if(count==n):
            return happynumber
        happynumber+=1

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

def isHappyPrime(n):
    if(isPrime(n)and isHappyNumber(n)):
        return True
    else:
        return False

def nthHappyPrime(n):
    if(n<0):
        return -1
    happyNumber=0
    count=0
    while count <=n:
        happyNumber +=1
        if(isHappyPrime(happyNumber)==True):
            count+=1
    return happyNumber

##############################################
## Prime Counting
##############################################
def almostEqual(d1, d2):
    epsilon = 0.000001
    return (abs(d2 - d1) < epsilon)

def pi(n):
    if(n<0):
        return 0
    number=0
    count=0
    while number <=n:
        if(isPrime(number)==True):
            count+=1
        number+=1
    return count

def h(n):
    total=0
    index=1
    if(n<0):
        return 0
    while index<=n:
        total+=1/float(index)
        index+=1
    return total

def estimatedPi(n):
    if(n>2):
        return int(round(n/(h(n)-1.5)))
    elif(n<=2):
        return 0

def estimatedPiError(n):
    if(n<=2):
        return 0
    else:
        return abs(estimatedPi(n)-pi(n))

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

######################################################################
# Place your (optional) additional tests here
######################################################################

def runMoreStudentTests():
    print "Running additional tests...",
    #### PUT YOUR ADDITIONAL TESTS HERE ####
    print "Passed!"

######################################################################
# Place your graphics solutions here!
######################################################################

from Tkinter import *
import math

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def drawCircle(canvas, x0, y0, x1, y1):
    width = x1 - x0
    if (width > 200):
        fill = "blue"
    else:
        fill = rgbString(147, 197, 114) # pistachio!
    canvas.create_oval(x0, y0, x1, y1, fill=fill, width=4)


def drawArrow(canvas, x0, y0, x1, y1):
    width = x1 - x0
    if (width > 200):
         canvas.create_rectangle(x0*4.25,y0+(y1-y0)/2.0,x0*5.75,y1,fill="red",width=0)
         canvas.create_polygon(x0*3,y0+(y1-y0)/2.0,x0*5,y0,x0*7,y0+(y1-y0)/2.0,fill="red",width=0)
    else:
         canvas.create_rectangle(x0+x1/5.75,y0,x0+x1/8.5,y0+(y1-y0)/2.0,fill="blue",width=0)
         canvas.create_polygon(x0+x1/4.5,y0+(y1-y0)/2.0,x0+x1/7,y1,x0+x1/13,y0+(y1-y0)/2.0,fill="blue",width=0)

def drawGradient(canvas, x0, y0, x1, y1):
    width = x1 - x0
    left=x0
    if (width > 200):
         for rgb in range(0,256,2):
               fill=rgbString(0, 0, rgb)
               canvas.create_rectangle(left,y0,x1,y1,fill=fill,width=0)
               left+=3
    else:
         for x in xrange(0,11):
               fill= rgbString(x*25,x*25,x*25)
               canvas.create_rectangle(left,y0,x1,y1,fill=fill,width=0)
               left+=18

def drawGrid(canvas, x0, y0, x1, y1):
    width = x1 - x0
    if (width > 200):
        text=1
        top=y0
        for row in range(1,5):
            left=x0
            for col in range(1,9):
                if(row%2==0):
                    if(text%2==0):
                        canvas.create_rectangle(left,top,x1,y1,fill=rgbString(255,92,92))
                        canvas.create_text(left+25,top+50, text=text)
                    else:
                        canvas.create_rectangle(left,top,x1,y1,fill=rgbString(147,112,219))
                        canvas.create_text(left+25,top+50, text=text)
                else:
                    if(text%2==0):
                        canvas.create_rectangle(left,top,x1,y1,fill=rgbString(147,112,219))
                        canvas.create_text(left+25,top+50, text=text)
                    else:
                        canvas.create_rectangle(left,top,x1,y1,fill=rgbString(255,92,92))
                        canvas.create_text(left+25,top+50, text=text)
                text+=1
                left+=50
            top+=100
    else:
        text=8
        top=y0
        for row in range(1,9):
            left=x0
            text=8-(row-1)
            for col in range(1,5):
                if(row%2==0):
                    if(col%2==0):
                        canvas.create_rectangle(left,top,x1,y1,fill="black")
                        canvas.create_text(left+25,top+12.5, text=text, fill="red")
                    else:
                        canvas.create_rectangle(left,top,x1,y1,fill="white")
                        canvas.create_text(left+25,top+12.5, text=text,fill="red")
                else:
                    if(col%2==0):
                        canvas.create_rectangle(left,top,x1,y1,fill="white")
                        canvas.create_text(left+25,top+12.5, text=text,fill="red")
                    else:
                        canvas.create_rectangle(left,top,x1,y1,fill="black")
                        canvas.create_text(left+25,top+12.5, text=text, fill="red")
                text+=8
                left+=50
            top+=25

def drawSpiral(canvas, x0, y0, x1, y1):
    width = (x1 - x0)
    height = (y1 - y0)
    r = min(width, height)/100.0
    r2= min(width,height)/58.0
    armangle=0
    angle=0
    if (width > 200):       
        for arm in range(0,28):
            cx = (x0 + x1)/2.0
            cy = (y0 + y1)/2.0
            armangle-=2*math.pi/28
            angle=armangle
            red=255
            green=255
            blue=0
            #angle+=(math.pi/4 )/ 32.0
            for circle in range(0,32):
                #fill="yellow"
                fill=rgbString(red,green,blue)
                canvas.create_oval(cx-r, cy-r,
                                   cx+r, cy+r,fill=fill,width=0)
                cx=cx+r2*math.cos(angle)
                cy=cy+r2*math.sin(angle)
                angle-=(math.pi/4)/ 16.0
                green-=255/32
                blue+=255/32
                red-=128/32
                #angle+=2*math.pi/28     
    else:
        for arm in range(0,28):
            cx = (x0 + x1)/2.0
            cy = (y0 + y1)/2.0
            armangle+=2*math.pi/28
            angle=armangle
            red=0
            green=255
            blue=0
            for circle in range(0,32):
                fill=rgbString(red,green,blue)
                canvas.create_oval(cx-r, cy-r,
                                   cx+r, cy+r,fill=fill,width=0)
                cx=cx+r2*math.cos(angle)
                cy=cy+r2*math.sin(angle)
                angle-=(math.pi/4 )/ 16.0
                #angle+=2*math.pi/28
                green-=255/32
                blue+=255/32

def randomCircleFun(canvas, left, top, width, height):
   #creates an image with random circles scattered with different sizes
   #and colors
   for outercirce in range(0,100):
       cx = (left + width)/ random.randint(1,100) #random center
       cy = (top + height)/random.randint(1,100)
       #generates a random radius for an outer circle
       outerRadius= min (width,height) / (random.randint(20,40))
       innerRadius= min (width,height)/ 100
       red=random.random() * 256 #generates random rgb value between 0 and 256
       green=random.random() * 256
       blue=random.random() * 256
       fill=rgbString(red,green,blue) #color of circle
       canvas.create_oval(cx-outerRadius, cy-outerRadius,
                             cx+outerRadius, cy+outerRadius,fill=fill,width=0)# creates outer circle
       while (outerRadius-innerRadius) > min(width, height) /100 : #creates inner circles until it reaches 
          canvas.create_oval(cx-innerRadius, cy-innerRadius,       #outercircle radius
                             cx+innerRadius, cy+innerRadius,fill=fill,width=0)
          innerRadius+=min (width,height) / (random.randint(80,100))
       


    

######################################################################
# Drivers: do not modify this code
######################################################################

def onButton(canvas, drawFn):
    canvas.data.drawFn = drawFn
    redrawAll(canvas)
    
def redrawAll(canvas):
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,canvas.data.width,canvas.data.height,fill="cyan")
    drawFn = canvas.data.drawFn
    if (drawFn):
        canvas.create_rectangle(50, 50, 450, 450, width=4)
        drawFn(canvas, 50, 50, 450, 450)
        canvas.create_rectangle(500, 150, 700, 350, width=4)
        drawFn(canvas, 500, 150, 700, 350)
        canvas.create_text(canvas.data.width/2,20, text=drawFn.__name__, fill="black", font="Arial 24 bold")

def graphicsMain():
    root = Tk()
    canvas = Canvas(root, width=750, height=500)
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width = 750
    canvas.data.height = 500
    buttonFrame = Frame(root)
    canvas.data.drawFns = [drawCircle, drawArrow, drawGradient, drawGrid, drawSpiral,randomCircleFun]
    canvas.data.drawFn = canvas.data.drawFns[0]
    for i in xrange(len(canvas.data.drawFns)):
        drawFn = canvas.data.drawFns[i]
        b = Button(buttonFrame, text=drawFn.__name__, command=lambda drawFn=drawFn:onButton(canvas, drawFn))
        b.grid(row=0,column=i)
    canvas.pack()
    buttonFrame.pack()
    redrawAll(canvas)
    root.mainloop()

######################################################################
# Main: you may modify this to run just the parts you want to test
######################################################################

def main():
    # include following line to autograde when you run this file
    execfile("hw2-public-grader.py", globals())
    runMoreStudentTests()
    graphicsMain()

if __name__ == "__main__":
    main()
