nr=int(input('confirm the no of resistors'))
import turtle
t=turtle
l=180
for i in range(0,nr):
  t.forward(100)
  t.left(45)
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.left(90)
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.left(90)
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.left(90)
  t.forward(10)
  t.right(90)
  t.forward(10)
  t.left(45)
  t.forward(25)
  t.penup()
  t.right(90)
  t.forward(25)
  t.right(90)
  t.forward(l)
  t.right(180)
  t.pendown()
  l=l+1
t.forward(90)
t.right(90)
t.forward(20)
t.right(180)
t.forward(40)
t.right(180)
t.forward(20)
t.left(90)
t.penup()
t.forward(5)
t.pendown()
t.right(90)
t.forward(10)
t.right(180)
t.forward(20)
t.right(180)
t.forward(10)
t.left(90)
t.forward(85)
t.left(90)

for i in range(0,nr):
  t.forward(25)
t.penup()
t.left(90)
t.forward(180)
t.left(90)
for i in range(0,nr):
  t.pendown()
  t.forward(25)
t.left(90)
t.penup()
t.forward(25)
t.pendown()





  
