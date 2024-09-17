from GameFrame import TextObject, Globals, RoomObject

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
    
    def set_score(self, amount):
        
        Globals.SCORE = amount
        self.text = str(Globals.SCORE)
        self.update_text()

class Lives(RoomObject):
    
    def __init__(self, room, x: int, y: int):
        
        # Intialises the lives object
        
        RoomObject.__init__(self, room, x, y)
        
        #set image
        self.lives_icon = []
        
        #load the various lives images into a live list
        for index in range(6):
            self.lives_icon.append(self.load_image(f"Lives_frames/Lives_{index}.png"))
        self.update_image()
    
    def update_image(self):
        # updates the number of lives on the UI
        
        self.set_image(self.lives_icon[Globals.LIVES], 125, 23)