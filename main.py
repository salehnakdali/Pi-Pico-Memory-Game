import time
from pimoroni import Button 
import random
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P4
import json

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P4)

#define buttons
button_a = Button(12) #MAGENTA
button_b = Button(13) #RED
button_x = Button(14) #YELLOW
button_y = Button(15) #GREEN

#define colors
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)
RED = display.create_pen(255, 0, 0)
genereatedColors = []
userChoice = []
score = 0
difficulty = 1
life = 5
#setup screen
def initScreen():
    display.set_pen(BLACK)
    w, h = display.get_bounds()
    display.rectangle(0, 0, w, h)

# clear a circle in the screen 
def clear():
    display.set_pen(BLACK)
    display.circle(120,120,75)
    display.update()
    
#startup intro
def intro():
    display.set_pen(WHITE)
    display.text("Memory Game",40,110,scale=3)
    display.update()
    time.sleep(1.5)
    x=1
    for i in range(1,60):
        x = x+10
        display.set_pen(MAGENTA)
        display.circle(x,60,25)
        #display.update()
        display.set_pen(YELLOW)
        display.circle(240-x,60,25)
        #display.update()
        display.set_pen(RED)
        display.circle(0+x,180,25)
        #display.update()
        display.set_pen(GREEN)
        display.circle(240-x,180,25)
        display.update()
    initScreen()
# show score and life
def showInfo():
    display.set_pen(BLACK)
    display.rectangle(0, 0, 69, 20)
    display.rectangle(180, 0, 69, 20)
    display.set_pen(WHITE)
    display.text("Score="+str(score),0,0,scale=2)
    display.set_pen(WHITE)
    display.text("Life="+str(life),175,0,scale=2)
    display.update()
# Show colors near the buttons
def showButtonsColor():
    display.set_pen(MAGENTA)
    display.circle(0,60,25)
    display.update()
    display.set_pen(YELLOW)
    display.circle(240,60,25)
    display.update()
    display.set_pen(RED)
    display.circle(0,180,25)
    display.update()
    display.set_pen(GREEN)
    display.circle(240,180,25)
    display.update()
    
#Visual Start count 
def showstart():
    if score == 0 and life ==5:
        display.set_pen(WHITE)
        display.text("Get Ready!",75,100,scale=2)
        display.update()
        time.sleep(1)
        clear()
        display.set_pen(WHITE)
        display.text("3",120,100,scale=3)
        display.update()
        time.sleep(1)
        clear()
        display.set_pen(WHITE)
        display.text("2",120,100,scale=3)
        display.update()
        time.sleep(1)
        clear()
        display.set_pen(WHITE)
        display.text("1",120,100,scale=3)
        display.update()
        time.sleep(1)
    
#print correct
def showCorrect():
        display.update()
        display.set_pen(WHITE)
        display.text("Correct!",75,100,scale=3)
        display.update()
        time.sleep(1)
        clear()    
#Print Nope!    
def showWrong():
        display.set_pen(WHITE)
        display.text("NOPE!",80,100,scale=3)
        display.update()
        time.sleep(1)
        clear()  
#Generate random colors with Time interval change based on difficulty
def showColor():
    for i in range(0,difficulty):
        clear()
        color = random.choice([MAGENTA,YELLOW,RED,GREEN])
        display.set_pen(color)
        display.circle(120,120,50)
        display.update()
        genereatedColors.append(color)
        deff = 1.5 - 0.1*(difficulty-2)
        time.sleep(deff)
        clear()
#  Final choice       
def lastAction():
    #initScreen()
    display.set_pen(MAGENTA)
    display.text("PlayAgain",150,220,scale=2)
    display.set_pen(WHITE)
    display.text("BYE ",10,220,scale=2)
    display.update()
    while True:
        if button_y.read():
            end = False
            return False
            break
        elif button_b.read():
            end =False
            return True
            break
# read user input       
def userInput():
    while True:
        #MAGENTA
        if button_a.read():
            userChoice.append(3)
            display.set_pen(MAGENTA)
            display.circle(0,60,35)
            display.update()
            time.sleep(0.2)
            display.set_pen(BLACK)
            display.circle(0,60,35)
            display.set_pen(MAGENTA)
            display.circle(0,60,25)
            display.update()
        #RED
        elif button_b.read():
            userChoice.append(6)
            display.set_pen(RED)
            display.circle(0,180,35)
            display.update()
            time.sleep(0.2)
            display.set_pen(BLACK)
            display.circle(0,180,35)
            display.set_pen(RED)
            display.circle(0,180,25)
            display.update()
        #YELLOW
        elif button_x.read():
            userChoice.append(4)
            display.set_pen(YELLOW)
            display.circle(240,60,35)
            display.update()
            time.sleep(0.2)
            display.set_pen(BLACK)
            display.circle(240,60,35)
            display.set_pen(YELLOW)
            display.circle(240,60,25)
            display.update()
        #GREEN
        elif button_y.read():
            userChoice.append(5)
            display.set_pen(GREEN)
            display.circle(240,180,35)
            display.update()
            time.sleep(0.2)
            display.set_pen(BLACK)
            display.circle(240,180,35)
            display.set_pen(GREEN)
            display.circle(240,180,25)
            display.update()
        else:
             if len(genereatedColors) == len(userChoice):
                 break
# Reset values
def resetValues():
    global genereatedColors,userChoice,score,difficulty,life
    genereatedColors = []
    userChoice = []
    score = 0
    difficulty = 1
    life = 5
    
# set up
initScreen()
display.set_font("bitmap8")
intro()

#start the Game
while True:
    showButtonsColor()
    showInfo()
    showstart()
    showColor()
    userInput()
    if genereatedColors == userChoice and life != 0 and score != 10:
        showCorrect()
        userChoice = []
        genereatedColors = []        
        score = score +1
        difficulty = difficulty+1
    elif genereatedColors != userChoice and life != 0 and score != 10:
        showWrong()
        life = life - 1
        userChoice = []
        genereatedColors = []
    elif score == 10 and life >= 0:
        clear()
        display.set_pen(WHITE)
        display.text("YOU WON !!!!",55,100,scale=3)
        display.text("SCORE "+str(score),65,150,scale=3)
        display.update()
        time.sleep(2)
        if lastAction() == True:
            break
        else:
            initScreen()
            resetValues()
    elif life == 0:
        clear()
        display.set_pen(WHITE)
        display.text("YOU LOST :(",55,100,scale=3)
        display.text("SCORE "+str(score),65,150,scale=3)
        display.update()
        time.sleep(2)
        if lastAction() == True:
            break
        else:
            initScreen()
            resetValues()
#END
initScreen()            
display.set_pen(WHITE)
display.text("BYE ",60,100,scale=10)
display.update()

