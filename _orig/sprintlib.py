import turtle
from random import *

# constants
RUNNER_SIZE = 20
TRACK_LEFT_X = -150
TRACK_RIGHT_X = 150
TRACK_TOP_Y = 100
TRACK_BOTTOM_Y = -100
DISTANCE = TRACK_RIGHT_X - TRACK_LEFT_X
STEP = 1

def prepareTrack(helper):
    ''' draws track, need turtle instance to handle track drawing '''
    #start
    # use TRACK_LEFT_X, TRACK_BOTTOM_Y and other constants
    # ...
    #finish
    # use TRACK_LEFT_X, TRACK_BOTTOM_Y and other constants
    # ...
    return True

def prepare(runner, helper):
    ''' prepares runner; also uses helper '''
    # initialise local variables
    # ...
    # display runner name
    # ...
    # initialise runner turtle instance
    # ...
    return True

def move(runner):
    ''' moves runner according to his speed '''
    # initialise local variables if needed
    # ...
    # move runner and record his current position
    # ...    
    return True

def board(helper, text):
    ''' displays message on the board; 
        uses dedicated turtle instance, this is becasue turtel instance is cleared before new message is displayed 
    '''
    # prepare 
    # ... draw text
    return True




