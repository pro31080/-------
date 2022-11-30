import turtle
from random import *
t=tuple
# constants
RUNNER_SIZE = 50
TRACK_LEFT_X = -400
TRACK_RIGHT_X = 400
TRACK_TOP_Y = 350
TRACK_BOTTOM_Y = -350
DISTANCE = TRACK_RIGHT_X - TRACK_LEFT_X
STEP = 1

def prepareTrack(helper):
    ''' draws track, need turtle instance to handle track drawing '''
    #start
    # use TRACK_LEFT_X, TRACK_BOTTOM_Y and other constants
    helper.width(3)
    helper.up()
    helper.goto(TRACK_LEFT_X,TRACK_BOTTOM_Y)
    helper.down()
    helper.goto(TRACK_LEFT_X,TRACK_TOP_Y)
    #finish
    # use TRACK_LEFT_X, TRACK_BOTTOM_Y and other constants
    helper.up()
    helper.goto(TRACK_RIGHT_X,TRACK_BOTTOM_Y)
    helper.down()
    helper.goto(TRACK_RIGHT_X,TRACK_TOP_Y)
    return True

def prepare(runner, helper):
    ''' prepares runner; also uses helper '''
    # initialise local variables
    t = runner["Object"]
    # display runner name
    # ...
    # initialise runner turtle instance
    t.color(runner["Color"])
    t.shape(runner["Shape"])
    t.up()
    t.goto(TRACK_LEFT_X,TRACK_BOTTOM_Y+RUNNER_SIZE*runner["Index"])
    runner["Position"]=TRACK_LEFT_X
    return True

def move(runner):
    ''' moves runner according to his speed '''
    # initialise local variables if needed
    # ...
    # move runner and record his current position
    t = runner["Object"]
    t.forward(runner["Speed"])
    runner["Position"] =runner["Position"] + runner["Speed"]
    return True

def board(helper, text):
    ''' displays message on the board; 
        uses dedicated turtle instance, this is becasue turtel instance is cleared before new message is displayed 
    '''
    # prepare 
    # ... draw text
    return True
