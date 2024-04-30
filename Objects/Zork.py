from GameFrame import RoomObject, Globals
import random


class Zork(RoomObject):
    """
    a class for the enemy
    """
    
    def __init__(self, room, x, y):
        # initialise the boss object
        RoomObject.__init__(self, room, x, y)
        
        image = self.load_image("Zork.png")
        self.set_image(image, 135, 165)
        
        self.y_speed = random.choice([-10,10])
    
    def keep_in_room(self):
        #keeps zork inside of room
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
    def step(self):
        # determine what happens to the zork on each tick of the game clock
        self.keep_in_room()