from app.ressources import *

class Soundbarre():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = (255, 240, 200)
        self.width = screen.get_width()/2
        self.height = 10
        
    def draw(self):
        pg.draw.rect(screen, self.color, (self.x, self.y - self.height/2, self.width, self.height))
        pg.draw.rect(screen, self.color, (int(self.x + self.width * pg.mixer.music.get_volume()), self.y - self.height*1.5, self.height, self.height*3))
        
    def volumeUp(self):
        pg.mixer.music.set_volume(pg.mixer.music.get_volume()+0.1)
    
    def volumeDown(self):
        pg.mixer.music.set_volume(pg.mixer.music.get_volume()-0.1)