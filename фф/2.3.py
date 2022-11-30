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
s = 300
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
s=200
color = "red"
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)

color = "green"
s = 100
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)
drawSqaure(t, color, 15,s)

time.sleep(5)