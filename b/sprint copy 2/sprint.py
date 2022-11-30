import turtle
import time
from random import *
from sprintlib import *

# helper turtle instance to draw track
helper = turtle.Turtle()

# helper  turtle instance to draw board
#boardHelper = ...

# prepare track
prepareTrack(helper)

# initialise runners

# runner1 = {
#     "Object": turtle.Turtle() , 
#     "Name":"a", 
#     "Shape":"turtle" , 
#     "Size":RUNNER_SIZE, 
#     "Color":"red", 
#     "Index":0, 
#     "Speed":randint(1,10), 
#     "Position":0
# }

runner1 = Runner()
runner1.Object = turtle.Turtle()
runner1.Name = "a"
runner1.Shape = "turtle" 
runner1.Size=RUNNER_SIZE
runner1.Color="red"
runner1.Index=0
runner1.Speed=1
runner1.SpeedMax=10
runner1.Position=0

runner2 = Runner()
runner2.Object = turtle.Turtle()
runner2.Name = "wa"
runner2.Shape = "turtle" 
runner2.Size=RUNNER_SIZE
runner2.Color="blue"
runner2.Index=1
runner2.Speed=1 
runner2.SpeedMax=10
runner2.Position=0

runner3 = Runner()
runner3.Object = turtle.Turtle()
runner3.Name = "wa"
runner3.Shape = "turtle" 
runner3.Size=RUNNER_SIZE
runner3.Color="red"
runner3.Index=2
runner3.Speed=1 
runner3.SpeedMax=10
runner3.Position=0

# runner2 = {
#     "Object":turtle.Turtle() , 
#     "Name":"A", 
#     "Shape": "turtle", 
#     "Size":RUNNER_SIZE, 
#     "Color":"blue", 
#     "Index":1, 
#     "Speed": randint(1,10), 
#     "Position":0
# }

# runner3 = {
#     "Object":turtle.Turtle() , 
#     "Name":"AF", 
#     "Shape": "turtle", 
#     "Size":RUNNER_SIZE, 
#     "Color":"orange", 
#     "Index":2, 
#     "Speed": randint(1,10), 
#     "Position":0
# }

# prepare runner

runner1.prepare(helper)
runner2.prepare(helper)
runner3.prepare(helper)


# display board message


time.sleep(1)

#loop to move"+"check runners
while runner1.Position<= TRACK_RIGHT_X and runner2.Position <= TRACK_RIGHT_X and runner3.Position <= TRACK_RIGHT_X  :
    runner1.move()
    runner2.move()
    runner3.move()

    # check if someone finished
    # ...
    #time.sleep(0.1)

time.sleep(1)

# check results and update board
#if ...: 
#     ...
# elif ...: 
#     ...
# else: 
#     ...

time.sleep(1)