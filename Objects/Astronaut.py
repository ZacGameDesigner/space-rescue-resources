from GameFrame import RoomObject
from GameFrame.Level import Level

class Astronaut(RoomObject):
    
    def __init__(self,room,x,y):
        """
        Initialise the astronaut instance
        """
        # include attirbutes and method from RoomObject
        RoomObject.__init__(self,room,x,y)
        
        # set image
        image = self.load_image("Astronaut.png")
        self.set_image(image,50,49)
        
        # set travel direction
        self.set_direction(180, 5)
        
        # handle events
        self.register_collision_object("Ship")
        
    def step(self):
        """
        Determines what happend to the astronaut on each tick of the game clock
        """
        self.outside_of_room()
    
    def handle_collision(self, other, other_type):
        #handles collision for Astronaut object
        if other_type == "Ship":
            self.room.astronaut_saved.play()
            self.room.delete_object(self)
            self.room.score.update_score(50)
    
    def outside_of_room(self):
        # removes astronauts when outside of room
        
        if self.x + self.width < 0:
            self.room.delete_object(self)
        
        