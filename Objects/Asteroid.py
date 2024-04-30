from GameFrame import RoomObject

class Asteroid(RoomObject):
    # zork dangerous obstacles
    
    def __init__(self, room, x, y):
        #initialise the asteroid object
        
        RoomObject.__init__(self, room, x, y)
        
        image = self.load_image("asteroid.png")
        self.set_image(image, 50, 49)