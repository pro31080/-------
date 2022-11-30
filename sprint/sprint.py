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
runner1 = {
    "Object": turtle.Turtle() , 
    "Name":"a", 
    "Shape":"turtle" , 
    "Size":RUNNER_SIZE, 
    "Color":"red", 
    "Index":0, 
    "Speed":randint(1,10), 
    "Position":0
}
runner2 = {
    "Object":turtle.Turtle() , 
    "Name":"A", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"blue", 
    "Index":1, 
    "Speed": randint(1,10), 
    "Position":0
}
runner3 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"orange", 
    "Index":2, 
    "Speed": randint(1,10), 
    "Position":0
}
runner4 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"red", 
    "Index":3, 
    "Speed": 1, 
    "Position":0
}
runner5 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"blue", 
    "Index":4, 
    "Speed": randint(1,10), 
    "Position":0
}
runner6 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"orange", 
    "Index":5, 
    "Speed": randint(1,10), 
    "Position":0
}
runner7 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"red", 
    "Index":6, 
    "Speed": randint(1,10), 
    "Position":0
}
runner8 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"blue", 
    "Index":7, 
    "Speed": randint(1,10), 
    "Position":0
}
runner9 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"orange", 
    "Index":8, 
    "Speed": randint(1,10), 
    "Position":0
}
runner10 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"red", 
    "Index":9, 
    "Speed": randint(1,10), 
    "Position":0
}
runner11 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"blue", 
    "Index":10, 
    "Speed": randint(1,10), 
    "Position":0
}
runner12 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"orange", 
    "Index":11, 
    "Speed": randint(1,10), 
    "Position":0
}
runner13 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"red", 
    "Index":12, 
    "Speed": randint(1,10), 
    "Position":0
}
runner14 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"blue", 
    "Index":13, 
    "Speed": randint(1,10), 
    "Position":0
}
runner15 = {
    "Object":turtle.Turtle() , 
    "Name":"AF", 
    "Shape": "turtle", 
    "Size":RUNNER_SIZE, 
    "Color":"orange", 
    "Index":14, 
    "Speed": randint(1,10), 
    "Position":0
}

# prepare runner
prepare(runner1,helper)
prepare(runner2,helper)
prepare(runner3,helper)
prepare(runner4,helper)
prepare(runner5,helper)
prepare(runner6,helper)
prepare(runner7,helper)
prepare(runner8,helper)
prepare(runner9,helper)
prepare(runner10,helper)
prepare(runner11,helper)
prepare(runner12,helper)
prepare(runner13,helper)
prepare(runner14,helper)
prepare(runner15,helper)

# display board message


time.sleep(1)

#loop to move"+"check runners
while runner1["Position"]<= TRACK_RIGHT_X and runner2["Position"] <= TRACK_RIGHT_X and runner3["Position"] <= TRACK_RIGHT_X and runner4["Position"]<= TRACK_RIGHT_X and runner5["Position"] <= TRACK_RIGHT_X and runner6["Position"] <= TRACK_RIGHT_X and runner7["Position"]<= TRACK_RIGHT_X and runner8["Position"] <= TRACK_RIGHT_X and runner9["Position"] <= TRACK_RIGHT_X and runner10["Position"] <= TRACK_RIGHT_X and runner11["Position"] <= TRACK_RIGHT_X and runner12["Position"] <= TRACK_RIGHT_X:
    move(runner1)
    move(runner2)
    move(runner3)
    move(runner4)
    move(runner5)
    move(runner6)
    move(runner7)
    move(runner8)
    move(runner9)
    move(runner10)
    move(runner11)
    move(runner12)
    move(runner13)
    move(runner14)
    move(runner14)
    move(runner15)

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


