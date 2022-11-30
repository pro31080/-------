import turtle
import time
t=turtle.Turtle()

def drawTriangle(t, color, penWidth,size):
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
def drawTrianglee(t, color, penWidth,size):
    """ my function
    """
    t.color(color)
    t.width(penWidth)

    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90) 
    t.forward(size)
    t.right(90)
    t.forward(size)

def drawTriangleee(t, color, penWidth,size):
    """ my function
    """
    t.color(color)
    t.width(penWidth)
    drawTrianglee(t, color, penWidth,size)
    drawTrianglee(t, color, penWidth,size)
    drawTrianglee(t, color, penWidth,size)
    drawTrianglee(t, color, penWidth,size)
    drawTrianglee(t, color, penWidth,size)
    drawTrianglee(t, color, penWidth,size)
    
def drawTriangles(t, color, penWidth,size):
    """ my function
    """
    drawTriangle(t, color, penWidth,size)
    drawTriangle(t, color, penWidth,size)
    drawTriangle(t, color, penWidth,size)
    drawTriangle(t, color, penWidth,size)
    drawTriangle(t, color, penWidth,size)
    drawTriangle(t, color, penWidth,size)

    return True
    
t.speed (200000)

yaScreen = turtle.Screen()
yaScreen.bgcolor("black")


color=("red")

drawTriangles(t, "color", 10,25)
drawTriangles(t, "color", 10,50)
drawTriangles(t,"color", 10,75)
drawTriangles(t, "color", 10,100)
drawTriangles(t,"color", 10,125)
drawTriangles(t, "color", 10,150)
drawTriangles(t,"color", 10,175)
drawTriangles(t, "color", 10,200)
drawTriangles(t,"color", 10,225)
drawTriangles(t, "color", 10,250)
drawTriangles(t,"color", 10,275)
drawTriangles(t, "color", 10,300)
drawTriangles(t, "color", 10,325)
drawTriangles(t, "color", 10,350)
drawTriangles(t, "color", 10,375)
    
drawTrianglese(t,"red")
yaScreen = turtle.Screen()
yaScreen.bgcolor("white")


yaScreen = turtle.Screen()
yaScreen.bgcolor("black")

t.color("green")
t.up()
t.goto(-375,300)
t.write("паутинка бабабуй",False,"left",font=("Arial",75,"normal"))
drawTriangles(t, "color", 5,375)

time.sleep(10)

