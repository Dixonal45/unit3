# by Allison Dixon
# last updated September 27, 2019
# writing Mississipi

import turtle

def set_up():
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-400, 0)
    turtle.pendown()
    turtle.lt(90)

def go_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.rt(180)

def m():
    turtle.color("turquoise")
    for x in range(3):
        turtle.fd(80)
        turtle.rt(90)
        turtle.fd(10)
        turtle.rt(90)
    turtle.lt(40)
    turtle.fd(30)
    turtle.lt(100)
    turtle.fd(30)
    turtle.rt(140)
    for x in range(2):
        turtle.fd(80)
        turtle.lt(90)
        turtle.fd(10)
        turtle.lt(90)

def i():
    for x in range(1):
        turtle.fd(80)
        turtle.lt(90)
        turtle.fd(5)
        turtle.rt(180)
        turtle.fd(20)
        turtle.rt(180)
        turtle.fd(5)
        turtle.lt(90)
        turtle.fd(80)
        turtle.lt(90)
        turtle.fd(5)
        turtle.rt(180)
        turtle.fd(20)

def s():
    turtle.fd(40)
    turtle.lt(90)
    for x in range(3):
        turtle.fd(40)
        turtle.lt(90)
        turtle.fd(10)
        turtle.lt(90)
    turtle.rt(90)
    turtle.fd(30)
    turtle.rt(90)
    for x in range(3):
        turtle.fd(40)
        turtle.rt(90)
        turtle.fd(10)
        turtle.rt(90)
    turtle.lt(90)
    turtle.fd(30)

def main():
    set_up()
    m()
    go_to(-320, 0)
    i()
    go_to(-290, 0)
    s()
    go_to(-230, 0)


main()

turtle.exitonclick()
