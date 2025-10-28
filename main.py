

from pyray import *
import random 

SIDE = 40
WIDTH = 20
HEIGHT = 20
snake = [[1,1],
         [2,1],
         [3,1]]
fruit=[WIDTH//2,HEIGHT//2]
vitesse = [1,0]
perdu = False
Score = 0
init_window(SIDE*WIDTH,SIDE*HEIGHT,"Mon jeu")
set_target_fps(10)

while not window_should_close() and perdu == False :
    begin_drawing()
    clear_background(WHITE)


    #jeu 

    if is_key_pressed(KEY_UP) and vitesse != [0,1]:
        vitesse = [0,-1]
    if is_key_pressed(KEY_DOWN) and vitesse != [0,-1]:
        vitesse = [0,1]
    if is_key_pressed(KEY_RIGHT) and vitesse != [-1,0]:
        vitesse = [1,0]
    if is_key_pressed(KEY_LEFT) and vitesse != [1,0]:
        vitesse = [-1,0]

 



    #animation
    vx,vy = vitesse
    hx,hy = snake[-1]
    new_head = [hx+vx,hy+vy]

    if new_head == fruit: 
        snake = snake + [new_head]
        fruit = [random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)]
        Score = Score + 1
    else : 
        snake = snake[1:]+[new_head]

    #condition de fin de partie
    if new_head[0]<0 or new_head[0]>=WIDTH or new_head[1]<0 or new_head[1]>=HEIGHT : 
        print("perdu")
        perdu=True
        
    if new_head in snake[:-1] : 
        print("perdu")
        perdu=True

   
   
    #dessin
    for i,(x,y) in enumerate(snake) : 
        color = DARKGREEN if i ==len(snake)-1 else GREEN
        draw_rectangle(x * SIDE, y * SIDE,SIDE-1,SIDE-1,color)

    draw_text(f"Score : {Score}",5,0,50,BLACK)

    draw_rectangle(fruit[0]*SIDE,fruit[1]*SIDE,SIDE,SIDE,RED)
        

    end_drawing()

while not is_key_pressed(KEY_UP):
    clear_background(WHITE)
    begin_drawing()
    draw_text("GAME OVER ", 100,100,100,RED)  
    draw_text(f"Score : {Score} ", 270,300,50,RED)  
    draw_text("press up ", 350,500,25,RED)   

    end_drawing() 


close_window()