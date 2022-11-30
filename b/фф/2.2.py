import turtle
import time
t=turtle.Turtle()

def drawSqaure(t, color, penWidth,size):
    """ my function
    """
    t.color(color)
    t.width(penWidth)

    t.right(60)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(120) 
    t.forward(size)

    return True
t.speed (10)

color = "blue"

drawSqaure(t, "blue", 15,300)
drawSqaure(t, "blue", 15,300)
drawSqaure(t, "blue", 15,300)
drawSqaure(t, "blue", 15,300)
drawSqaure(t, "blue", 15,300)
drawSqaure(t, "blue", 15,300)

drawSqaure(t, "red", 15,200)
drawSqaure(t, "red", 15,200)
drawSqaure(t, "red", 15,200)
drawSqaure(t, "red", 15,200)
drawSqaure(t, "red", 15,200)
drawSqaure(t, "red", 15,200)

time.sleep(5)