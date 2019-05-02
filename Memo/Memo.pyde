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
        
        #Sound Effects for Memo   
        self.musmh = audioPlayer.loadFile(path + "/Sounds/memo_h.wav")
        self.musbc0 = audioPlayer.loadFile(path + "/Sounds/first_pick.wav")
        self.musbc1 = audioPlayer.loadFile(path + "/Sounds/bad_second_pick.wav")
        self.musbc2 = audioPlayer.loadFile(path + "/Sounds/good_second_pick.wav")
        
        #Backgrounds
        self.menubg = loadImage(path + "/Images/main_menu.png")
        self.helpbg = loadImage(path + "/Images/help_menu.png")
        self.gamebg = loadImage(path + "/Images/game.png")
        self.lbbg = loadImage(path + "/Images/leaderboards.png")
        
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
        
        #Button Variables
        self.LBbutton_isvisible = True
        self.GameButton_isvisible = True
        self.ExitButton_isvisible = True
        self.HelpButton_isvisible = True
        self.SoundButton_isvisible = True
        self.MenuButton_isvisible = False
        
        #Game Variables
        self.inmenu = True
        self.inhelp = False
        self.inmemo = False
        self.inleaderboards = False
        self.mute = False
        self.win = False
        self.board = []

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
        self.musclick.rewind()
        self.musclick.play()
        self.inhelp = True
        self.inmemo = False
        self.inleaderboards = False
        self.inmenu = False
        self.display_help()
        
    def menubuttonclick(self):
        self.musclick.rewind()
        self.musclick.play()
        self.inhelp = False
        self.inmemo = False
        self.inleaderboards = False
        self.inmenu = True
        self.display_menu()

    def LBbuttonclick(self):
        self.musclick.rewind()
        self.musclick.play()
        self.inhelp = False
        self.inmemo = False
        self.inleaderboards = True
        self.inmenu = False
        self.display_lb()
    
    def gamebuttonclick(self):
        self.musclick.rewind()
        self.musclick.play()
        self.inhelp = False
        self.inmemo = True
        self.inleaderboards = False
        self.inmenu = False
        self.display_game()
    
    def exitbuttonclick(self):
        exit()
        
    def drawboard(self):
        for rowid in range(3):
            row = []
            for colid in range(6):
                row.append(Memo(rowid, colid))
            self.board.append(row)
    
    def display_menu(self):
        self.LBbutton_isvisible = True
        self.GameButton_isvisible = True
        self.ExitButton_isvisible = True
        self.HelpButton_isvisible = True
        self.SoundButton_isvisible = True
        self.MenuButton_isvisible = False
        imageMode(CENTER)
        image(self.menubg, 960, 540)
        image(self.leaderboardsbutton, 511, 540)
        image(self.gamebutton, 960, 540)
        image(self.exitbutton, 1409, 540)
        image(self.helpbutton, 724, 989)
        image(self.mutebutton, 960, 989)
    
    def display_help(self):
        self.LBbutton_isvisible = False
        self.GameButton_isvisible = False
        self.ExitButton_isvisible = False
        self.HelpButton_isvisible = False
        self.SoundButton_isvisible = True
        self.MenuButton_isvisible = True
        imageMode(CENTER)
        image(self.menubg, 960, 540)
        image(self.helpbg, 960, 540)
        image(self.mutebutton, 960, 989)
        image(self.backtomenubutton, 1196, 989)
    
    def display_lb(self):
        self.LBbutton_isvisible = False
        self.GameButton_isvisible = False
        self.ExitButton_isvisible = False
        self.HelpButton_isvisible = False
        self.SoundButton_isvisible = True
        self.MenuButton_isvisible = True
        imageMode(CENTER)
        image(self.lbbg, 960, 540)
        image(self.mutebutton, 960, 989)
        image(self.backtomenubutton, 1196, 989)
    
    def display_game(self):
        self.LBbutton_isvisible = False
        self.GameButton_isvisible = False
        self.ExitButton_isvisible = False
        self.HelpButton_isvisible = False
        self.SoundButton_isvisible = True
        self.MenuButton_isvisible = True
        imageMode(CENTER)
        image(self.gamebg, 960, 540)
        image(self.mutebutton, 960, 989)
        image(self.backtomenubutton, 1196, 989)
    
    def highlight_and_sound(self):
        imageMode(CENTER)
        if self.LBbutton_isvisible == True and 371 <= mouseX <= 651 and 380 <= mouseY <= 700:
            image(self.leaderboardsbutton_h, 511, 540)
            self.musbh.play()
        elif self.GameButton_isvisible == True and 820 <= mouseX <= 1100 and 380 <= mouseY <= 700:
            image(self.gamebutton_h, 960, 540)
            self.musbh.play()
        elif self.ExitButton_isvisible == True and 1269 <= mouseX <= 1549 and 380 <= mouseY <= 700:
            image(self.exitbutton_h, 1409, 540)
            self.musbh.play()
        elif self.HelpButton_isvisible == True and 674 <= mouseX <= 774 and 939 <= mouseY <= 1039:
            image(self.helpbutton_h, 724, 989)
            self.musbh.play()
        elif self.SoundButton_isvisible == True and 910 <= mouseX <= 1010 and 939 <= mouseY <= 1039:
            image(self.mutebutton_h, 960, 989)
            self.musbh.play()
        elif self.MenuButton_isvisible == True and 1146 <= mouseX <= 1246 and 939 <= mouseY <= 1039:
            image(self.backtomenubutton_h, 1196, 989)
            self.musbh.play()
        else:
            self.musbh.rewind()        

class Memo():
    
    def __init__(self, rowid, colid):
        #Variables
        self.rowid = rowid
        self.colid = colid
        self.id = id
        
        #Images
        self.img = loadImage(path + "/Images/" + str(id) + ".png")
        self.frame = loadImage(path + "/Images/frame.png")
        self.hidden = loadImage(path + "/Images/hidden.png")
        self.highlight = loadImage(path + "/Images/hidden_highlight.png")
   
def display_frames():
    if game.inmemo == True:
        for rowid in range(3):
            for colid in range(6):
                imageMode(CENTER)
                image(game.board[rowid][colid].frame, 335 + 250 * colid, 280 + 250 * rowid)
    else:
        return

game = Game()

def setup():
    fullScreen()
    frameRate(360)
    game.musbg_play()
    game.drawboard()
    game.display_menu()

def draw():
    imageMode(CORNER)
    cursor(loadImage(path + "/Images/cursor.png"), 0, 0)
    if game.inmenu == True:
        game.display_menu()
    elif game.inleaderboards == True:
        game.display_lb()
    elif game.inmemo == True:
        game.display_game()
    elif game.inhelp == True:
        game.display_help() 
    game.highlight_and_sound()

def mouseClicked():
    imageMode(CENTER)
    if game.LBbutton_isvisible == True and 371 <= mouseX <= 651 and 380 <= mouseY <= 700:
        game.LBbuttonclick()
    elif game.GameButton_isvisible == True and 820 <= mouseX <= 1100 and 380 <= mouseY <= 700:
        game.gamebuttonclick()
    elif game.ExitButton_isvisible == True and 1269 <= mouseX <= 1549 and 380 <= mouseY <= 700:
        game.exitbuttonclick()
    elif game.HelpButton_isvisible == True and 674 <= mouseX <= 774 and 939 <= mouseY <= 1039:
        game.helpbuttonclick()
    elif game.SoundButton_isvisible == True and 910 <= mouseX <= 1010 and 939 <= mouseY <= 1039:
        game.mutebuttonclick()
    elif game.MenuButton_isvisible == True and 1146 <= mouseX <= 1246 and 939 <= mouseY <= 1039:
        game.menubuttonclick()
