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

class Runner:
    Object:turtle= turtle.Turtle() , 
    Name:str="a"
    Shape:str="turtle" , 
    Size:int=RUNNER_SIZE, 
    Color:str="red", 
    Index:int=0, 
    Speed:int=7
    SpeedMax: int=10
    Position:int=0
    def prepare(self, helper):
        ''' prepares runner; also uses helper '''
        # initialise local variables
        t = self.Object
        # display runner name
        # ...
        # initialise runner turtle instance
        t.color(self.Color)
        t.shape(self.Shape)
        t.up()
        t.goto(TRACK_LEFT_X,TRACK_BOTTOM_Y+RUNNER_SIZE*self.Index)
        self.Position = TRACK_LEFT_X
        return True
    def move(self):
        ''' moves runner according to his speed '''
        # initialise local variables if needed
        # ...
        # move runner and record his current position
        t = self.Object
        s = randint(self.Speed,self.SpeedMax)
        t.forward(s)
        self.Position =self.Position + s
        return True


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




def board(helper, text):
    ''' displays message on the board; 
        uses dedicated turtle instance, this is becasue turtel instance is cleared before new message is displayed 
    '''
    # prepare 
    # ... draw text
    return True
