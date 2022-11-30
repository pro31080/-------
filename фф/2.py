import turtle
import time

def drawSqaure(t, color, penWidth):
    """ my function
    """
    t.color(color)
    t.width(penWidth)

    t.forward(300)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(300)
    t.right(90)    

    return True


t=turtle.Turtle()
t.shape("turtle")

t.speed(1)
t.color("red")

t.width(50)

t.forward(300)
t.right(90)
t.forward(300)
t.right(90)
t.forward(300)
t.right(90)
t.forward(300)
t.right(90)

t.color("blue")

t.width(25)

t.forward(300)
t.right(90)
t.forward(300)
t.right(90)
t.forward(300)
t.right(90)
t.forward(300)
t.right(90)



# t.color("red")

# t.width(12)

# t.forward(300)
# t.right(90)
# t.forward(300)
# t.right(90)
# t.forward(300)
# t.right(90)
# t.forward(300)
# t.right(90)

drawSqaure(t, "red", 12)
time.sleep(5)

