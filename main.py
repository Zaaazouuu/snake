

from pyray import *
import random 


#===configuration===

SIDE = 40
WIDTH = 20
HEIGHT = 20

init_window(SIDE*WIDTH,SIDE*HEIGHT,"Mon jeu")
set_target_fps(10)
Score = 0
snake = []
fruit = []
fruit_magique=[]
timer=0
vitesse = []
perdu = False

#===fonctions===

def start_game():
    """relance le jeu"""
    global snake,fruit,vitesse,Score,perdu,fruit_magique,timer
    snake = [[1,1],
         [2,1],
         [3,1]]
    fruit=[WIDTH//2,HEIGHT//2]
    fruit_magique=None
    vitesse = [1,0]
    perdu = False
    Score = 0
    timer=0

def spawn_food():
    """fait spawn les fruits"""
    global timer
    if random.randint(1,5)==1:
        timer = 50
        return ([random.randint(0, WIDTH - 1),
            random.randint(0, HEIGHT - 1)],[random.randint(0, WIDTH - 1),
            random.randint(0, HEIGHT - 1)])
    else : 
        return ([random.randint(0, WIDTH - 1),
            random.randint(0, HEIGHT - 1)],None)

def handle_input(vitesse):
    """gere les inputs"""
    if is_key_pressed(KEY_UP) and vitesse != [0,1]:
        vitesse = [0,-1]
    if is_key_pressed(KEY_DOWN) and vitesse != [0,-1]:
        vitesse = [0,1]
    if is_key_pressed(KEY_RIGHT) and vitesse != [-1,0]:
        vitesse = [1,0]
    if is_key_pressed(KEY_LEFT) and vitesse != [1,0]:
        vitesse = [-1,0]
    return(vitesse)

def end_game():
    """affiche le game over et la fin du jeu"""
    clear_background(WHITE)
    begin_drawing()
    draw_text("GAME OVER ", 100,100,100,RED)  
    draw_text(f"Score : {Score} ", 270,300,50,RED)  
    draw_text("press SPACE to restart", 250,500,25,RED)
    end_drawing() 

def draw(snake):
    """réalise le dessin"""
    for i,(x,y) in enumerate(snake) : 
        color = DARKGREEN if i ==len(snake)-1 else GREEN
        draw_rectangle(x * SIDE, y * SIDE,SIDE-1,SIDE-1,color)
        draw_text(f"Score : {Score}",5,0,50,BLACK)
        draw_rectangle(fruit[0]*SIDE,fruit[1]*SIDE,SIDE,SIDE,RED)
        if not fruit_magique==None : 
            draw_rectangle(fruit_magique[0]*SIDE,fruit_magique[1]*SIDE,SIDE,SIDE,PURPLE)

def collision(new_head,snake):
    """test les conditions de fin de partie"""
    global perdu
    if new_head[0]<0 or new_head[0]>=WIDTH or new_head[1]<0 or new_head[1]>=HEIGHT : 
            print("perdu")
            perdu=True
        
    if new_head in snake[:-1] : 
        print("perdu")
        perdu=True

#===debut du jeu===

start_game()
while not window_should_close():
    if perdu == False :        
        #jeu 
        vitesse = handle_input(vitesse)
        #animation
        vx,vy = vitesse
        hx,hy = snake[-1]
        new_head = [hx+vx,hy+vy]
        if timer>0:
            timer-=1
            if timer<=0:
                fruit_magique=None
        if new_head == fruit: 
            snake = snake + [new_head]
            fruit,fruit_magique = spawn_food()
            Score = Score + 1
        elif new_head == fruit_magique:
            snake = snake + [new_head]
            fruit,fruit_magique=spawn_food()
            Score = Score + int(timer/5)+1

        else : 
            snake = snake[1:]+[new_head]
        #condition de fin de partie
        collision(new_head,snake)
        #dessin
        begin_drawing()
        clear_background(WHITE)
        draw(snake)
        end_drawing()
    else : 
        end_game()
        if is_key_pressed(KEY_SPACE):
            start_game()



close_window()