# koch-snowflake.py

import turtle

def kN(length, n):
    if (n == 1):
        turtle.forward(length)
    else:
        kN(length/3.0, n-1)
        turtle.left(60)
        kN(length/3.0, n-1)
        turtle.right(120)
        kN(length/3.0, n-1)
        turtle.left(60)
        kN(length/3.0, n-1)

def kochSnowflake(length, n):
    for step in range(3):
        kN(length, n)
        turtle.right(120)

turtle.delay(0)
turtle.speed(0)
turtle.penup()
turtle.goto(-300,100)
turtle.pendown()

turtle.pencolor("black")
kN(300, 4) # same as k4(300)

turtle.pencolor("blue")
kochSnowflake(300, 4)

turtle.penup()
turtle.goto(-250,50)
turtle.pendown()
turtle.pencolor("red")
kochSnowflake(200, 7)
turtle.done()
