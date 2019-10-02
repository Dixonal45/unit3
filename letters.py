# by Allison Dixon
# last updated September 27, 2019
# This program writes "Mississippi"

import turtle


def set_up():
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-315, 0)
    turtle.pendown()
    turtle.lt(90)


def go_to(x, y, z):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.rt(z)


def m():
    turtle.color("cornflower blue")
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


def p():
    for x in range(3):
        turtle.fd(80)
        turtle.rt(90)
        turtle.fd(10)
        turtle.rt(90)
    turtle.lt(90)
    turtle.fd(30)
    turtle.rt(90)
    for x in range(3):
        turtle.fd(35)
        turtle.rt(90)
        turtle.fd(10)
        turtle.rt(90)
    turtle.lt(90)
    turtle.fd(20)


def main():
    set_up()
    m()
    go_to(-230, 0, 180)
    i()
    go_to(-200, 0, 180)
    s()
    go_to(-140, 0, 0)
    s()
    go_to(-80, 0, 270)
    i()
    go_to(-50, 0, 180)
    s()
    go_to(10, 0, 0)
    s()
    go_to(70, 0, 270)
    i()
    go_to(100, 0, 90)
    p()
    go_to(155, 0, 90)
    p()
    go_to(215, 0, 90)
    i()
    go_to(250, 0, 0)


main()

turtle.exitonclick()
