# week 4 Loops

from turtle import *

def square():
    for counter in range(4):
        forward(100)
        right(90)



def triangle():
    for counter in range(2):
        forward(140)
        left(90)



def pentagon():
    for counter in range(5):
        forward(100)
        right(72)



def hexagon():
    for counter in range(6):
        forward(100)
        right(60)

def rectangle():
    for counter in range(2):
        forward(200)
        right(90)
        forward(100)
        right(90)

def envelop():
    rectangle()
    right(45)
    triangle()

envelop()


done()
