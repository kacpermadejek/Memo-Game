add_library("minim")
import os, random, time
path = os.getcwd()
audioPlayer = Minim(this)

class Game:
    
    def __init__(self):
        #Sound Effects
        self.musbg = audioPlayer.loadFile(path + "/Sounds/bgmusic.mp3")
        self.musbh = audioPlayer.loadFile(path + "/Sounds/button_h.wav")
        self.musclick = audioPlayer.loadFile(path + "/Sounds/click.wav")
        self.muswin = audioPlayer.loadFile(path + "/Sounds/win.wav")
        self.mussg = audioPlayer.loadFile(path + "/Sounds/startgame.mp3")
        self.musqg = audioPlayer.loadFile(path + "/Sounds/quitgame.mp3")
        
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
        self.swbg = loadImage(path + "/Images/score_window.png")
        self.twbg = loadImage(path + "/Images/time_window.png")
        
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
        self.LBbutton_ish = False
        self.GameButton_ish = False
        self.ExitButton_ish = False
        self.HelpButton_ish = False
        self.SoundButton_ish = False
        self.MenuButton_ish = False
        
        #Game Variables
        self.inmenu = True
        self.inhelp = False
        self.inmemo = False
        self.inleaderboards = False
        self.mute = False
        self.displayname = False
        self.win = False
        self.board = []
        self.name = ''
        self.score = 0

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
            self.mussg.mute()
            self.musqg.mute()
            self.musmh.mute()
            self.musbc0.mute()
            self.musbc1.mute()
            self.musbc2.mute()
            
        elif self.mute == False:
            self.musbg.unmute()
            self.musbh.unmute()
            self.musclick.unmute()
            self.muswin.unmute()
            self.mussg.unmute()
            self.musqg.unmute()
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
        
    def menubuttonclick(self):
        if self.inmemo == False or game.win == True:
            self.musclick.rewind()
            self.musclick.play()
        else:
            self.musqg.rewind()
            self.musqg.play()
        game.displayname = False
        self.inhelp = False
        self.inmemo = False
        self.inleaderboards = False
        self.inmenu = True
        

    def LBbuttonclick(self):
        self.musclick.rewind()
        self.musclick.play()
        self.inhelp = False
        self.inmemo = False
        self.inleaderboards = True
        self.inmenu = False
        update_lb()
    
    def gamebuttonclick(self):
        self.mussg.rewind()
        self.mussg.play()
        self.win = False
        self.name = ''
        self.score = 0
        self.inhelp = False
        self.inmemo = True
        self.inleaderboards = False
        self.inmenu = False
        
        starting_time = time.time()
        global starting_time
    
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
        display_lb_scores()
    
    def display_game(self):
        self.LBbutton_isvisible = False
        self.GameButton_isvisible = False
        self.ExitButton_isvisible = False
        self.HelpButton_isvisible = False
        self.SoundButton_isvisible = True
        imageMode(CENTER)
        image(self.gamebg, 960, 540)
        image(self.mutebutton, 960, 989)
        image(self.twbg, 960, 540)
        if game.win == False:
            self.MenuButton_isvisible = True
            image(self.backtomenubutton, 1196, 989)
        elif game.win == True:
            self.MenuButton_isvisible = False
    
    def highlight_and_sound(self):
        self.LBbutton_ish = False
        self.GameButton_ish = False
        self.ExitButton_ish = False
        self.HelpButton_ish = False
        self.SoundButton_ish = False
        self.MenuButton_ish = False
        imageMode(CENTER)
        if self.LBbutton_isvisible == True and 371 <= mouseX <= 651 and 380 <= mouseY <= 700:
            image(self.leaderboardsbutton_h, 511, 540)
            self.LBbutton_ish = True
            self.musbh.play()
        elif self.GameButton_isvisible == True and 820 <= mouseX <= 1100 and 380 <= mouseY <= 700:
            image(self.gamebutton_h, 960, 540)
            self.GameButton_ish = True
            self.musbh.play()
        elif self.ExitButton_isvisible == True and 1269 <= mouseX <= 1549 and 380 <= mouseY <= 700:
            image(self.exitbutton_h, 1409, 540)
            self.ExitButton_ish = True
            self.musbh.play()
        elif self.HelpButton_isvisible == True and 674 <= mouseX <= 774 and 939 <= mouseY <= 1039:
            image(self.helpbutton_h, 724, 989)
            self.HelpButton_ish = True
            self.musbh.play()
        elif self.SoundButton_isvisible == True and 910 <= mouseX <= 1010 and 939 <= mouseY <= 1039:
            image(self.mutebutton_h, 960, 989)
            self.SoundButton_ish = True
            self.musbh.play()
        elif self.MenuButton_isvisible == True and 1146 <= mouseX <= 1246 and 939 <= mouseY <= 1039:
            image(self.backtomenubutton_h, 1196, 989)
            self.MenuButton_ish = True
            self.musbh.play()
        elif (self.LBbutton_ish == False 
        and self.GameButton_ish == False 
        and self.ExitButton_ish == False 
        and self.HelpButton_ish == False 
        and self.SoundButton_ish == False 
        and self.MenuButton_ish == False):
            self.musbh.rewind()
        else:
            pass            

class Memo():
    
    def __init__(self, rowid, colid):
        #Variables
        self.rowid = rowid
        self.colid = colid
        self.id = id
        self.is_assigned = False
        self.is_chosen = False
        self.is_visible = False
        self.is_highlighted = False
        
        #Images
        self.hidden = loadImage(path + "/Images/hidden.png")
        self.highlight = loadImage(path + "/Images/hidden_h.png")

    def show_image(self):
        return loadImage(path + "/Images/" + str(self.id) + ".png")
    
def assign_id():
    
    id_list = []
    
    for i in range(9):
        a = random.randint(1, 40)
        while a in id_list:
            a = random.randint(1, 40)
        id_list.append(a)
    id_list = id_list*2
    
    while len(id_list) != 0:
        r = random.randint(0, 2)
        c = random.randint(0, 5)
        info = id_list.pop(random.randrange(len(id_list)))
        while game.board[r][c].is_assigned == True:
            r = random.randint(0, 2)
            c = random.randint(0, 5)
        game.board[r][c].id = info
        game.board[r][c].is_assigned = True

def clear_id():
    for rowid in range(3):
        for colid in range(6):
            game.board[rowid][colid].is_assigned = False 

def clear_is_chosen():
    for rowid in range(3):
        for colid in range(6):
            game.board[rowid][colid].is_chosen = False 

def clear_is_visible():
    for rowid in range(3):
        for colid in range(6):
            game.board[rowid][colid].is_visible = False 

def ask_for_name():
    if game.displayname == True:
        imageMode(CENTER)
        image(game.swbg, 960, 540)
        textAlign(LEFT)
        fill(250)
        text(game.name, 860, 720)
    else:
        pass

def show_score():
    if game.displayname == True:
        imageMode(CENTER)
        image(game.twbg, 960, 540)
        display_time()
    else:
        pass
        
def save_score():
     file = open("scores.txt", "a")
     file.write('|' + game.name)
     file.write('|' + str(game.score))
     file.close()

def sort_lists(list1, list2): 
    pair = zip(list2, list1) 
    output = [x for _, x in sorted(pair)]
    return output  

def update_lb():
    file = open("scores.txt", "r")
    contents = file.read().split('|')
    file.close()
    contents = contents[2:]
    
    names_list = []
    scores_list = []
    leaderboards_list = []

    for i in range(len(contents)/2):
        name = contents[2 * i]
        names_list.append(name)
        score = contents[1 + 2 * i]
        scores_list.append(score)
    
    for i in range(len(scores_list)):
        scores_list[i] = round(float(scores_list[i]), 3)
    
    sorted_names_list = sort_lists(names_list, scores_list)
    sorted_scores_list = sorted(scores_list)
    
    for i in range(len(sorted_names_list)):
        lb_score = []
        lb_score.append(sorted_names_list[i])
        lb_score.append(sorted_scores_list[i])
        leaderboards_list.append(lb_score)
    leaderboards_list = leaderboards_list[:7]

    global leaderboards_list, sorted_scores_list

def display_lb_scores():
    fill(104, 0 ,114)
    place = 1
    for i in range(len(leaderboards_list)):
        textAlign(CENTER)
        if i == 0:
            text(place, 500, 430 + i * 80)
        elif leaderboards_list[i][1] != leaderboards_list[i-1][1]:
            place += 1
            text(place, 500, 430 + i * 80)
        elif leaderboards_list[i][1] == leaderboards_list[i-1][1]:
            text(place, 500, 430 + i * 80)
        text(leaderboards_list[i][0], 960, 430 + i * 80)
        textAlign(LEFT)
        text(leaderboards_list[i][1], 1300 , 430 + i * 80) 
        

def display_time():
    fill(250)
    if game.win == True:
        game.score = stop_time - starting_time
        textAlign(CENTER)
        text(game.score, 960, 95)
    else:
        textAlign(CENTER)
        text(time.time() - starting_time, 960, 95)
   
def display_hidden():
    for rowid in range(3):
        for colid in range(6):
            imageMode(CENTER)
            image(game.board[rowid][colid].hidden, 335 + 250 * colid, 280 + 250 * rowid)

def display_img():
    for rowid in range(3):
        for colid in range(6):
            imageMode(CENTER)
            if game.board[rowid][colid].is_visible == True or game.board[rowid][colid].is_chosen == True:
                image(game.board[rowid][colid].show_image(), 335 + 250 * colid, 280 + 250 * rowid)
                        
def highlight_and_sound_memo():
    for rowid in range(3): 
        for colid in range(6): 
            game.board[rowid][colid].is_highlighted = False
            if (game.board[rowid][colid].is_visible == False) and (game.board[rowid][colid].is_chosen == False): 
                if (335 + 250 * colid - 80 <= mouseX <= 335 + 250 * colid + 80) and (280 + 250 * rowid - 80 <= mouseY <= 280 + 250 * rowid + 80):
                    image(game.board[rowid][colid].highlight, 335 + 250 * colid, 280 + 250 * rowid)
                    game.board[rowid][colid].is_highlighted = True
                    game.musmh.play()
                else:
                    pass
            else:
                pass
                
    highlighted = False
    for rowid in range(3): 
        for colid in range(6): 
            if game.board[rowid][colid].is_highlighted == True:
                highlighted = True
    if highlighted == False:
        game.musmh.rewind()

def check_is_chosen():
    chosen = 0
    for rowid in range(3):
        for colid in range(6):
            if game.board[rowid][colid].is_chosen == True:
                chosen += 1
                if chosen == 1:
                    r1 = rowid
                    c1 = colid
                elif chosen == 2:
                    r2 = rowid
                    c2 = colid
                else:
                    pass

    if chosen == 1:
        game.musbc0.rewind()
        game.musbc0.play()
    elif chosen == 2:
        if game.board[r1][c1].id == game.board[r2][c2].id:
            game.board[r1][c1].is_visible = True
            game.board[r2][c2].is_visible = True
            clear_is_chosen()
            game.musbc2.rewind()
            game.musbc2.play()
        else:
            game.musbc1.rewind()
            game.musbc1.play()
            clear_is_chosen()    
            return chosen        

def check_win():
    uncovered = 0
    for rowid in range(3):
        for colid in range(6):
            if game.board[rowid][colid].is_visible == False:
                uncovered += 1
    if uncovered == 0:
        game.win = True
        game.displayname = True
        game.muswin.rewind()
        game.muswin.play()
        stop_time = time.time()
        global stop_time
    else:
        pass
                        
game = Game()

def setup():
    fullScreen()
    font = loadFont("SlugfestNF-70.vlw")
    textFont(font, 70)
    frameRate(60)
    game.musbg_play()
    game.drawboard()

def draw():
    imageMode(CORNER)
    cursor(loadImage(path + "/Images/cursor.png"), 0, 0)
    if game.inmenu == True:
        game.display_menu()
    elif game.inleaderboards == True:
        game.display_lb()
    elif game.inmemo == True:
        game.display_game()
        display_hidden()
        highlight_and_sound_memo()
        display_img()
        display_time()
        if game.win == True:
            ask_for_name()
            show_score()
        else:
            pass
    elif game.inhelp == True:
        game.display_help() 
    game.highlight_and_sound()

def keyReleased():
    if game.displayname == True:
        if key == BACKSPACE or key == DELETE:
            game.musmh.rewind()
            game.musmh.play()
            game.name = game.name[0:len(game.name)-1]
        elif key == ENTER:
            save_score()
            game.menubuttonclick()
        elif len(game.name) < 11:
            if str(key) == '65535':
                return
            elif str(key).upper() in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']:
                game.musmh.rewind()
                game.musmh.play()
                game.name += str(key)
            else:
                pass
        else:
            pass
    else:
        pass

def mouseClicked():
    imageMode(CENTER)
    if game.LBbutton_isvisible == True and 371 <= mouseX <= 651 and 380 <= mouseY <= 700:
        game.LBbuttonclick()
    elif game.GameButton_isvisible == True and 820 <= mouseX <= 1100 and 380 <= mouseY <= 700:
        assign_id()
        game.gamebuttonclick()
    elif game.ExitButton_isvisible == True and 1269 <= mouseX <= 1549 and 380 <= mouseY <= 700:
        game.exitbuttonclick()
    elif game.HelpButton_isvisible == True and 674 <= mouseX <= 774 and 939 <= mouseY <= 1039:
        game.helpbuttonclick()
    elif game.SoundButton_isvisible == True and 910 <= mouseX <= 1010 and 939 <= mouseY <= 1039:
        game.mutebuttonclick()
    elif game.MenuButton_isvisible == True and 1146 <= mouseX <= 1246 and 939 <= mouseY <= 1039:
        clear_id()
        clear_is_chosen()
        clear_is_visible()
        game.menubuttonclick()
    elif game.inmemo == True:
        for rowid in range(3): 
            for colid in range(6): 
                if (game.board[rowid][colid].is_visible == False) and (game.board[rowid][colid].is_chosen == False): 
                    if (335 + 250 * colid - 80 <= mouseX <= 335 + 250 * colid + 80) and (280 + 250 * rowid - 80 <= mouseY <= 280 + 250 * rowid + 80):
                        game.board[rowid][colid].is_chosen = True
                        check_is_chosen()
                        check_win()
