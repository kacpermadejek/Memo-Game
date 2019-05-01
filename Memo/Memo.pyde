add_library("minim")
import os, random
path = os.getcwd()
audioPlayer = Minim(this)

class Game:
    def __init__(self):
        self.bgmusic = audioPlayer.loadFile(path + "/Sounds/bgmusic.mp3")
        self.mute = False
    
    def bgmusicplay(self):
        self.bgmusic.rewind()
        self.bgmusic.loop()
    
    def mutebutton(self):
        self.mute = not self.mute

class Memo:
    def __init__(self, rowid, colid, id):
        self.rowid = rowid
        self.colid = colid
        self.id = id
        self.img = loadImage(path + "/Images/" + str(id) + ".png")

def setup():
  fullScreen()
  background(loadImage(path + "/Images/" + "menu_display" + ".png"))

game = Game()
game.bgmusicplay()

def draw():
    cursor(loadImage(path + "/Images/cursor.png"), 0, 0)

def mouseClicked():
    pass
