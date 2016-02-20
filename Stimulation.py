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

class Stimulation:
    global TopRate, BotRate, LeftRate, RightRate
    # Set up stimulus's frequency
    TopRate =   5              # Hz
    BotRate = 10
    LeftRate = 15
    RightRate = 20

    def __init__(self):
        self._running = True

        # Initialize screen
        self.screen = get_default_screen()

        # Get dimension of the screen
        w = self.screen.size[0]
        h = self.screen.size[1]

        # Set dimension of the targets
        HSize = 100
        VSize = 50

        # Number of trials
        self.numTrial = 3

        # Initialize Targets
        self.TopTarget = Target2D(size= (HSize, VSize),
                                  color= (1.0, 1.0, 1.0, 1.0),
                                  position=(w/2, h*0.8))

        self. BotTarget = Target2D(size= (HSize, VSize),
                                   color= (1.0, 1.0, 1.0, 1.0),
                                   position=(w/2, h*0.2))

        self.LeftTarget = Target2D(size= (VSize, HSize),
                                   color= (1.0, 1.0, 1.0, 1.0),
                                   position=(w*0.2, h/2))

        self.RightTarget = Target2D(size= (VSize, HSize),
                                    color= (1.0, 1.0, 1.0, 1.0),
                                    position=(w*0.8, h/2))

        # Message
        self.text = Text(text='Please wait for next trial...',
                         color=(1.0, 0.5, 0.5),
                         position=(w/2, h*0.8),
                         font_size=50,
                         anchor='center',
                         on=False)

        # Arrows
        self.arrow = TextureStimulus(texture=Texture('images\left2.bmp'),
                                     position=(w/2, h/2),
                                     anchor='center',
                                     on=False)

        # Viewports to stick graphical objects to screen
        self.viewport1 = Viewport(screen=self.screen,
                                  stimuli=[self.TopTarget, self.BotTarget, self.LeftTarget, self.RightTarget])

        self.viewport2 = Viewport(screen=self.screen,
                                  stimuli=[self.text, self.arrow])

        # Presentations (for controlling timing)
        self.p = Presentation(go_duration=(3, 'seconds'), viewports=[self.viewport1])

        self.p2 = Presentation(go_duration=(2, 'seconds'), viewports=[self.viewport2])

    def on_init(self):
        # Set screen's background color
        self.screen.set(bgcolor=(0., 0., 0.)) # black

        # Set control's parameters and corresponding function. Controlling targers
        self.p.add_controller(self.TopTarget, 'on',     FunctionController(during_go_func=self.topFlick))
        self.p.add_controller(self.BotTarget, 'on',     FunctionController(during_go_func=self.botFlick))
        self.p.add_controller(self.LeftTarget, 'on',    FunctionController(during_go_func=self.leftFlick))
        self.p.add_controller(self.RightTarget, 'on',   FunctionController(during_go_func=self.rightFlick))

        # Controlling others
        # self.p2.add_controller(self.text, 'on',         FunctionController(during_go_func=self.appear))
        self.p2.add_controller(self.arrow, 'on',        FunctionController(during_go_func=self.arrow_appear))

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        for i in range(0,self.numTrial):
            self.p.go()
            self.p2.go()

    #################################################
    # Controlling methods: Flickering               #
    #################################################
    def topFlick(self,t):
        return int(t*TopRate*2.0) % 2

    def botFlick(self,t):
        return int(t*BotRate*2.0) % 2

    def leftFlick(self,t):
        return int(t*LeftRate*2.0) % 2

    def rightFlick(self,t):
        return int(t*RightRate*2.0) % 2

    def arrow_appear(self, t):
        flag = True
        if flag:
            #self.writedata(t, 1)
            flag = False

        if self.p.is_in_go_loop():
            return False
        else:
            return True

    #################################################
    # Writing data methods                          #
    #################################################
    def on_writing(self):
        # Open file for writing data
        self.file = open("Recordingfile.txt", "w")

    def on_close(self):
        self.file.close()

    def writedata(self, time, target_flag):
        line = str(time) + '\t' + str(target_flag) + '\n'
        file.write(line)

"""
    Main
"""
if __name__ == "__main__":
    exp = Stimulation()
    exp.on_execute()