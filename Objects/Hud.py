from GameFrame import TextObject, Globals
from GameFrame.Level import Level

class Score(TextObject):
    # class for displaying score
    
    def __init__(self, room, x: int, y: int, text=None):
        #intialises the score object
        
        TextObject.__init__(self, room, x, y, text)
        
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255, 255, 255)
        self.bold = False
        self.update_text()
    
    def update_score(self, change):
        #updates the score and redraws the text
        
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()