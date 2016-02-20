#!/usr/bin/env python
"""Display 4
"""

from VisionEgg import *
start_default_logging(); watch_exceptions()

from VisionEgg.Core import *
from VisionEgg.FlowControl import Presentation, FunctionController
from VisionEgg.MoreStimuli import *
from VisionEgg.Text import Text
from VisionEgg.Textures import *
import time


# Set up stimulus's frequency
TopRate =   5              # Hz
BotRate = 10
LeftRate = 15
RightRate = 20

# Setting screen
screen = get_default_screen()
screen.set( bgcolor= (0., 0., 0.) ) # black
w = screen.size[0]
h = screen.size[1]

HSize = 100
VSize = 50
# Target stimulus
TopTarget = Target2D(size= (HSize, VSize),
                     color= (1.0, 1.0, 1.0, 1.0),
                     position=(w/2, h*0.8))

BotTarget = Target2D(size= (HSize, VSize),
                     color= (1.0, 1.0, 1.0, 1.0),
                     position=(w/2, h*0.2))

LeftTarget = Target2D(size= (VSize, HSize),
                      color= (1.0, 1.0, 1.0, 1.0),
                      position=(w*0.2, h/2))

RightTarget = Target2D(size= (VSize, HSize),
                       color= (1.0, 1.0, 1.0, 1.0),
                       position=(w*0.8, h/2))
# Message
text = Text(text='Please wait for next trial...',
            color=(1.0, 0.5, 0.5),
            position=(w/2, h*0.8),
            font_size=50,
            anchor='center',
            on=False)

# Direction
filename = "left.bmp"
texture = Texture(filename)
arrow = TextureStimulus(texture=texture,
                        position=(w/2, h/2),
                        anchor='center',
                        on=False)

viewport1 = Viewport(screen=screen,
                     stimuli=[TopTarget, BotTarget, LeftTarget, RightTarget])

viewport2 = Viewport(screen=screen,
                     stimuli=[text, arrow])

p = Presentation(go_duration=(3,'seconds'),viewports=[viewport1])

p2 = Presentation(go_duration=(2,'seconds'), viewports=[viewport2])

# Flickering method
def TopFlick(t):
    return int(t*TopRate*2.0) % 2

def BotFlick(t):
    return int(t*BotRate*2.0) % 2

def LeftFlick(t):
    return int(t*LeftRate*2.0) % 2

def RightFlick(t):
    return int(t*RightRate*2.0) % 2

def appear():
    return True

def appear_t(t):
    if p.is_in_go_loop():
        return False
    else:
        return True

def disapp(t):
    return False

p.add_controller(TopTarget,'on', FunctionController(during_go_func=TopFlick))
p.add_controller(BotTarget,'on', FunctionController(during_go_func=BotFlick))
p.add_controller(LeftTarget,'on', FunctionController(during_go_func=LeftFlick))
p.add_controller(RightTarget,'on', FunctionController(during_go_func=RightFlick))
p2.add_controller(text, 'on', FunctionController(during_go_func=appear_t))
p2.add_controller(arrow, 'on', FunctionController(during_go_func=appear_t))


numTrial = 3

for i in range(0,numTrial):
    p.go()
    p2.go()

