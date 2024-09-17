from GameFrame import TextObject
import pygame

class Text(TextObject):
    # class for displaying score
    
    def __init__(self, room, x: int, y: int, text=None):
        #intialises the score object
        
        TextObject.__init__(self, room, x, y, text)
        
        
        # Check for key press event
        
        self.handle_key_events = True     
        self.size = 40
        self.font = 'Arial Black'
        self.colour = (255, 255, 255)
        self.bold = False
        self.update_text()

    
    def update_score(self, change):
        #updates the score and redraws the text
        
        self.text = (self.text)
        self.update_text()
        
    def key_pressed(self, key):
        """
        if the key pressed is space, the game will start
        """
        
        if key[pygame.K_SPACE]:
            self.room.running = False