# program written for Session 4
# Anything written after # is ignored by the computer
# We can use it to annotate programs to make them more readable

from turtle import *

# this line says we are using the "turtle" library of functions
# remember to use this for turtle graphics in Python


def square():
    color('orange', 'blue')
    begin_fill()
    forward (100) 
    right (90)
    forward (100) 
    right (90) 
    forward (100) 
    right (90) 
    forward (100)
    right (90)
    end_fill()
    done()

square()

penup()
right(90)
forward (150)
pendown()

def triangle():
    color('red', 'green')
    begin_fill()
    forward (100) 
    right (120)
    forward (100) 
    right (120) 
    forward (100) 
    right (120)
    end_fill()
    done()

triangle()    
