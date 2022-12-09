from turtle import *

t = Turtle()

t.left(36)
def stern(t, size):


    for i in range(5):
        t.forward(size)
        t.right(36+180)
        if size!=300:
            stern(t, size/10)




stern(t, 300)
done()
