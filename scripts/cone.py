#!/usr/bin/python3
import turtle
s = turtle.getscreen()
t = turtle
t.shape('turtle')
t.shapesize(2.5)
t.color('red')
t.pencolor('black')
for i in range(1, int(input("How big should the cone be? (Recommended range is 100-250.) "))):
  t.circle(i)
t.hideturtle()