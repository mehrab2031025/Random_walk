from turtle import *
from random import choice, random
def random_walk(obj):
    direction = [0, 90, 180, 270]
    obj.pensize(20)
    obj.speed(100)
    while True:
        (x,y) = obj.pos()
        if x > -700 and x < 700 and y > -500 and y < 500:
            obj.pencolor(random(), random(), random())
            obj.forward(50)
            obj.right(choice(direction))
        else:
            obj.teleport(0, 0)







timmy = Turtle()
timmy.shape("turtle")
random_walk(timmy)








screen = Screen()
screen.exitonclick()
