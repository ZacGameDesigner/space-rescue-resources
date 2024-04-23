from GameFrame import RoomObject
import pygame

class Ship(RoomObject):
    """
    a class for the player avater (ship)
    
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        #set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)
        
        self.handle_key_events = True
        
    def key_pressed(self, key):
        #respond to keypress up and down
        
        if key[pygame.K_w]:
            self.y_speed = -10
        elif key[pygame.K_s]:
            self.y_speed = 10