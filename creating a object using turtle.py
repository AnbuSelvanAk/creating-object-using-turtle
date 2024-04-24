from turtle import *
x=Turtle()
dist=10
w=7
h=10
x.penup()
for i in range(h):
    for j in range(w):
        x.dot()
        x.forward(dist)
    x.backward(dist * w)
    x.right(90)
    x.forward(dist)
    x.left(90)