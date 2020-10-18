import turtle
from turtle import*

wn = turtle.Screen()
wn.bgcolor("black")
t= Turtle()
t.shape("turtle")
t.speed(0)
t.color("white")
def circle (t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawCircle(t,size,n):
  for i in range (n):
    circle(t,size)
    t.right(360/n)
drawCircle(t,100,10)
t.hideturtle()

t2=Turtle()
t2.shape("turtle")
t2.speed(0)
t2.color("yellow")
def circle (t2,size):
    for i in range(4):
        t2.circle(size)
        size=size-10
def drawCircle(t2,size,n):
  for i in range (n):
    circle(t2,size)
    t2.right(360/n)
drawCircle(t2,100,10)
t2.hideturtle()

t3=Turtle()
t3.shape("turtle")
t3.speed(0)
t3.color("blue")
def circle (t3,size):
    for i in range(4):
        t3.circle(size)
        size=size-5
def drawCircle(t3,size,n):
  for i in range (n):
    circle(t3,size)
    t3.right(360/n)
drawCircle(t3,100,10)
t3.hideturtle()

t4=Turtle()
t4.shape("turtle")
t4.speed(0)
t4.color("orange")
def circle (t4,size):
    for i in range(4):
        t4.circle(size)
        size=size-19
def drawCircle(t4,size,n):
  for i in range (n):
    circle(t4,size)
    t4.right(360/n)
drawCircle(t4,100,10)
t4.hideturtle()

t5=Turtle()
t5.shape("turtle")
t5.speed(0)
t5.color("purple")
def circle (t5,size):
    for i in range(4):
        t5.circle(size)
        size=size-5
def drawCircle(t5,size,n):
  for i in range (n):
    circle(t5,size)
    t5.right(360/n)
drawCircle(t5,100,10)
t5.hideturtle()

t6=Turtle()
t6.shape("turtle")
t6.speed(2)
t6.color("orange")
style=("courier",32,"bold")
t6.up()
t6.setposition(-70,200)
t6.down()
t6.write('HIT137',font=style)
t6.hideturtle()

turtle.exitonclick()