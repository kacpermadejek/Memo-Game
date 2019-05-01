add_library("minim")
import os, random
path = os.getcwd()
audioPlayer = Minim(this)

class Game:
    
    def __init__(self):
        #Sound Effects
        self.musbg = audioPlayer.loadFile(path + "/Sounds/bgmusic.mp3")
        self.musbh = audioPlayer.loadFile(path + "/Sounds/button_h.wav")
        self.musclick = audioPlayer.loadFile(path + "/Sounds/click.wav")
        self.muswin = audioPlayer.loadFile(path + "/Sounds/win.wav")
        
        #Sound Effects for Memo Class (Inheritance)    
        self.musmh = audioPlayer.loadFile(path + "/Sounds/memo_h.wav")
        self.musbc0 = audioPlayer.loadFile(path + "/Sounds/first_pick.wav")
        self.musbc1 = audioPlayer.loadFile(path + "/Sounds/bad_second_pick.wav")
        self.musbc2 = audioPlayer.loadFile(path + "/Sounds/good_second_pick.wav")
        
        #Backgrounds
        self.mainmenu = loadImage(path + "/Images/main_menu.png")
        self.helpmenu = loadImage(path + "/Images/help_menu.png")
        self.gamemenu = loadImage(path + "/Images/game.png")
        
        #Big Buttons
        self.leaderboardsbutton = loadImage(path + "/Images/icon_leaderboards.png")
        self.leaderboardsbutton_h = loadImage(path + "/Images/icon_leaderboards_h.png")
        self.gamebutton = loadImage(path + "/Images/icon_start.png")
        self.gamebutton_h = loadImage(path + "/Images/icon_start_h.png")
        self.exitbutton = loadImage(path + "/Images/icon_exit.png")
        self.exitbutton_h = loadImage(path + "/Images/icon_exit_h.png")
        
        #Small Buttons
        self.helpbutton = loadImage(path + "/Images/icon_help.png")
        self.helpbutton_h = loadImage(path + "/Images/icon_help_h.png")
        self.mutebutton = loadImage(path + "/Images/icon_mute.png")
        self.mutebutton_h = loadImage(path + "/Images/icon_mute_h.png")
        self.backtomenubutton = loadImage(path + "/Images/icon_backtomenu.png")
        self.backtomenubutton_h = loadImage(path + "/Images/icon_backtomenu_h.png")
        
        #Variables
        self.mute = False
        self.help = False
        self.win = False

    def musbg_play(self):
            self.musbg.rewind()
            self.musbg.loop()
    
    def mutebuttonclick(self):
        self.mute = not self.mute
        if self.mute == True:
            self.musbg.mute()
            self.musbh.mute()
            self.musclick.mute()
            self.muswin.mute()
            self.musmh.mute()
            self.musbc0.mute()
            self.musbc1.mute()
            self.musbc2.mute()
            
        elif self.mute == False:
            self.musbg.unmute()
            self.musbh.unmute()
            self.musclick.unmute()
            self.muswin.unmute()
            self.musmh.unmute()
            self.musbc0.unmute()
            self.musbc1.unmute()
            self.musbc2.unmute()
        
    def helpbuttonclick(self):
        if self.mute == False:
            self.musclick.rewind()
            self.musclick.play()
        self.help = True
        image(self.helpmenu, 960, 540)
        
    def menubuttonclick(self):
        if self.mute == False:
            self.musclick.rewind()
            self.musclick.play()
        self.help = False
        image(self.mainmenu, 960, 540)

class Memo(Game):
    
    def __init__(self, rowid, colid, id):
        self.rowid = rowid
        self.colid = colid
        self.id = id
        self.img = loadImage(path + "/Images/" + str(id) + ".png")
        
game = Game()
game.musbg_play()

def setup():
    fullScreen()
    background(game.mainmenu)

def draw():
    imageMode(CORNER)
    cursor(loadImage(path + "/Images/cursor.png"), 0, 0)
    imageMode(CENTER)

def mouseClicked():
    game.helpbuttonclick()
