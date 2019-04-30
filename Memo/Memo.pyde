add_library("minim")
import os, random
path = os.getcwd()
audioPlayer = Minim(this)

class Memo:
    def __init__(self, rowid, colid, id):
        self.rowid = rowid
        self.colid = colid
        self.id = id
        self.img = loadImage(path + "/Images/" + str(id) + ".png")

def setup():
  fullScreen()
  background(33)

def draw():
    pass

def mouseClicked():
    pass
    
