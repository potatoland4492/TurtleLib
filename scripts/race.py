#!/usr/bin/python
import time
import random
import turtle
def race():
  s = turtle.getscreen()
  t = turtle
  t.shapesize(2.5)
  t.shape('turtle')
  t.pensize(5)
  t.pu()
  t.goto(-500, 200)
  t.pd()
  t.fd(1000)
  t.pu()
  t.lt(90)
  t.fd(50)
  t.pd()
  t.bk(100)
  t.pu()
  t.goto(-500, -200)
  t.rt(90)
  t.pd()
  t.fd(1000)
  t.pu()
  t.lt(90)
  t.fd(50)
  t.pd()
  t.bk(100)
  t.pu()
  t.home()
  g = turtle.Turtle()
  g.shapesize(2.5)
  g.shape('turtle')
  g.pensize(5)
  g.color('green')
  g.pu()
  g.goto(-500, 200)
  g.pd()
  b = turtle.Turtle()
  b.shapesize(2.5)
  b.shape('turtle')
  b.pensize(5)
  b.color('blue')
  b.pu()
  b.goto(-500, -200)
  b.pd()
  input("Setup complete. Press `Enter` to start the game.")
  while g.xcor() < 500 and b.xcor() < 500:
    time.sleep(0.5)
    g.fd(random.randint(10, 100))
    time.sleep(0.5)
    b.fd(random.randint(10, 100))
  if g.xcor() >= 500 and b.xcor() >= 500:
    print("Both players tied!")
  elif g.xcor() >= 500 and b.xcor() < 500:
    print("The green player won!")
  elif b.xcor() >= 500 and g.xcor() < 500:
    print("The blue player won!")