from GameFrame import Level, Globals
from Objects import Score, Text
import pygame

class InfoScreen(Level):
    """
    Initial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background3.jpg")
    
        self.list = ["How to play the game:", "1. W is up and S is down", "2. Capture the astronauts, DO NOT SHOOT THEM!!!","3. Destroy astroids before the take all your lives", "4. Have fun"]
        
        for i in range(len(self.list)):
            self.add_room_object(Text(self, 100, 30 + 50 * i, self.list[i]))

            
