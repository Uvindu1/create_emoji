import turtle

emo = turtle.Turtle()
# meda raumak adina eka

emo.up()
emo.goto(0, 100)
emo.down()

# circle eka kahaparting fill karana eka
emo.begin_fill()
emo.pendown() #penup() it will stop drawing when you move the turtle , pendown() is the default state of turtle,memagin sahathika karanawa
emo.fillcolor('yellow')
emo.circle(100)
emo.end_fill()

#katata adlawa raum bagaya adima kirima
emo.up()
emo.goto(-67, -40)
emo.setheading(-60)# anshaka ganak dakwa adinna kiyana eka
emo.width(5)
emo.down()
emo.circle(80, 120)
emo.fillcolor("black")

#ass deka adima
for i in range(-35,105,70):
    emo.up()
    emo.goto(i, 35)
    emo.setheading(0)
    emo.down()
    emo.begin_fill()
    emo.circle(10)
    emo.end_fill()
emo.penup()#makes sure that the moving object that you've created does not draw anything on the window
emo.goto(0,-150)


turtle.mainloop()
























