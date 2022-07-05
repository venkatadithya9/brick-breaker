from paddle import *
from ball import *
from brick import *
from input import input_to
from grid import *
from border import *
from powerup import *
import time
import os
import sys
import random


os.system("clear")
bgnd = Grid(HEIGHT, WIDTH)
border = Border()
border.create_border(bgnd.show_grid())
paddle = Paddle(0)
paddle.print_paddle(bgnd.show_grid())
#setup bricks
bricks = []
collided = []
powerups = []

for i in range(len(layout1)):
    if (i in range(0,44)) or (i in range(88,132)):
        layout1[i] = True

for i in range(len(layout2)):
    if (i%22 <=8 and i<75) or (i%22>=13 and i<88):
        layout2[i] = True
    
    if i in range(132, 154):
        layout2[i] = True
    
    if (i%22 == 10 or i%22 == 11) and (i in range(75,153)):
        layout2[i] = True


for i in range(len(layout3)):
    #figure out limiting unbreakable type to some small number
    if (i %22 == 0 and i<180) or (i%22 == 21 and i<198) or (i%22 == 2 and i<113):
        layout3[i] = True
    if (i%22 == 1 and i< 134) or (i%22 == 20 and i<153) or (i%22 == 19 and i<130):
        layout3[i] = True
    if (i%22 == 3 and i< 92) or (i%22 == 18 and i<107) or (i%22 == 4 and i<71):
        layout3[i] = True
    if (i%22 == 5 and i< 50) or (i%22 == 6 and i<29) or (i%22 == 7 and i==7):
        layout3[i] = True
    if (i%22 == 17 and i< 84) or (i%22 == 16 and i<61) or (i%22 == 15 and i<38) or (i%22 == 14 and i==14):
        layout3[i] = True
    if (i in range(30,36)) or (i in range(53,57)) or (i==76 or i==77 or  i<21):
        layout3[i] = True

layout = layout1

for i in range(len(layout)):
    if layout[i]:
        type = (random.randint(0, 1000))%4
        brick_obj = Brick(type, i)
        bricks.append(brick_obj)

for brick in bricks:
    brick.print_brick(bgnd.show_grid())

#ball.print_ball(bgnd.show_grid())
print(CYAN+"\t\t\t\t\t***************************Game Start*************************"+RESET)
strtime = round(time.time())
curtime = time.time()
started = False
free = True
stuck = False
ref = 0.1

ball = Ball(paddle.get_x(), paddle.get_y()-2, 0)
ball.print_ball(bgnd.show_grid())
gap = 0
pressed = 0
stat= "init"
levels = True
level = 1
move = False
movedto = 0

print(Back.MAGENTA)
for i in range(4):
    for j in range(WIDTH):
        print(' ', end='')
    print()
print(Back.RESET)

while True:
    
    if time.time() - curtime >= ref:
        curtime = time.time()
        if started:
            gap += 1
            ball.path_manage(bgnd.show_grid(), paddle)
            if (ball.get_y() >= paddle.get_y() - 1) and (gap > 2):
                # find newx and newy
                newx = ball.get_x()
                newy = ball.get_y()
                chk = ball.check_paddlecoll(newx, newy, paddle)
                if chk == 100:
                    if(LIVES>1):
                        LIVES -= 1
                        os.system("aplay music/lifelost.wav -q &")
                        powerups.clear()
                        started = False
                        #ball.set_xvel(0)
                        #ball.set_pos(paddle.get_x(), paddle.get_y() - 2, bgnd.show_grid())
                        ball.erase_ball(bgnd.show_grid())
                        ball = Ball(paddle.get_x(), paddle.get_y()-2, 0)
                        ball.print_ball(bgnd.show_grid())

                    else:
                        #print(ball.get_debug())
                        #print(collided)
                        print(RED+"\t\t\t\t\t\t******Game ended******"+RESET)
                        os.system("killall aplay music/gameover.wav -q &")
                        break
                    

                else:
                    if stuck:
                        ball.set_stick(True)
                        ball.set_pos(paddle.get_x(), paddle.get_y() - 2, bgnd.show_grid())
                    else:
                        ball.set_stick(False)
                        ball.set_yvel(0 - ball.get_yvel()) 
                        ball.set_xvel(ball.get_xvel() + chk)
                    if move:
                        for brick in bricks:
                            brick.erase_brick(bgnd.show_grid())
                        for brick in bricks:
                            id = brick.get_id()
                            movedto = ((int)(id + 22/22))*2 + 5
                            layout[id] = False
                            #brick.erase_brick(bgnd.show_grid())
                            #brick.set_y(brick.get_y() + 2)
                            brick.set_id(id + 22)
                            layout[id + 22] = True
                            #brick.print_brick(bgnd.show_grid())
                        for brick in bricks:
                            brick.print_brick(bgnd.show_grid())
                        if brick.get_y() >= 34:
                            print(RED+"\t\t\t\t\t\t******Game ended******"+RESET)
                            os.system("killall aplay music/gameover.wav -q &")
                            break
            duration = round(curtime) - strtime
            
            if (duration > 22 and duration<46) or (duration > 68 and duration < 91) or (duration > 113 and duration < 135):
                    move = True
            
            if levels:

                if duration >= 135:
                    print(WHITE+"\t\t\t\t\t\t******TIME UP******"+RESET)
                    os.system("killall aplay music/gameover.wav -q &")
                    break
                elif duration in range(44,46):
                    #move = False
                    layout = layout2
                    level = 2
                    powerups.clear()
                    for brick in bricks:
                        brick.erase_brick(bgnd.show_grid())
                    
                    bricks.clear()

                    for i in range(len(layout)):
                        if layout[i]:
                            type = (random.randint(0, 1000))%4
                            brick_obj = Brick(type, i)
                            bricks.append(brick_obj)

                    for brick in bricks:
                        brick.print_brick(bgnd.show_grid())
                elif duration in range(89,91):
                    #move = False
                    layout = layout3
                    level = 3
                    powerups.clear()
                    for brick in bricks:
                        brick.erase_brick(bgnd.show_grid())
                    
                    bricks.clear()

                    for i in range(len(layout)):
                        if layout[i]:
                            type = (random.randint(0, 1000))%4
                            brick_obj = Brick(type, i)
                            bricks.append(brick_obj)

                    for brick in bricks:
                        brick.print_brick(bgnd.show_grid())
               

            for brick in bricks:
                if brick.get_strength() > 0 and layout[brick.get_id()]:
                    brick.erase_brick(bgnd.show_grid())
                    brick.change_colour()
                    brick.print_brick(bgnd.show_grid())
                    if brick.check_coll(ball):
                        collided.append(brick.get_id())
                        os.system("aplay music/coin.wav -q &")
                        brick.set_changes(-1)
                        chk = brick.set_strength(ball)
                        if chk == 1:
                            brick.erase_brick(bgnd.show_grid())
                            bricks.remove(brick)
                            layout[brick.get_id()] = False
                            SCORE += 1
                            if brick.get_id() != 1:
                                SCORE += 1
                            type = random.randint(1,8)
                            if type == 1:
                                powerup = Speedball(brick.get_x(), brick.get_y())
                            if type == 2:
                                powerup = Expandpaddle(brick.get_x(), brick.get_y())
                            if type == 3:
                                powerup = Shrinkpaddle(brick.get_x(), brick.get_y())
                            if type == 4:
                                powerup = Thruball(brick.get_x(), brick.get_y())
                            if type == 5:
                                powerup = Paddlegrab(brick.get_x(), brick.get_y())
                            if type < 6:
                                powerups.append(powerup)
                        elif chk == 0:
                            brick.erase_brick(bgnd.show_grid())
                            brick.print_brick(bgnd.show_grid())   #change brick colour
                            SCORE += 1

        inp = input_to()
        
        if inp == 'q':
            print(RED+"\t\t\t\t QUIT GAME")
            break

        if inp == 'a':
            if started == False:
                started = True
            paddle.move_paddle(bgnd.show_grid(),-1) 
        elif inp == 'd':
            if started == False:
                started = True
            paddle.move_paddle(bgnd.show_grid(),1)
        elif inp == 'l':
            paddle.erase_paddle(bgnd.show_grid())
            paddle.set_len(paddle.get_len() + 2)
            paddle.print_paddle(bgnd.show_grid())
        elif inp == 'k':
            if paddle.get_len()-2 > 1:
                paddle.erase_paddle(bgnd.show_grid())
                paddle.set_len(paddle.get_len() - 2)
                paddle.print_paddle(bgnd.show_grid())
        elif inp == ' ':
            if ref == 0.1:
                ref = 0.05
            else:
                ref = 0.1
        elif inp == 'r':
            if ball.get_thru():
                ball.set_thru(False)
            else:
                ball.set_thru(True)
        elif inp == 'p':
            pass
        elif inp == '0':
            levels = False
        else:
            paddle.set_vel(0)
            paddle.move_paddle(bgnd.show_grid(), 0)

        for powerup in powerups:
            stat = powerup.get_active()
            type = powerup.get_type()
            if stat == 0:
                powerup.move_pow(bgnd.show_grid())
                if powerup.get_y() >= paddle.get_y() - 2:
                    if type == 1:
                        chk = powerup.check_coll(paddle)
                    elif type == 2:
                        chk = powerup.check_coll(paddle, bgnd.show_grid())
                    elif type == 3:
                        chk = powerup.check_coll(paddle, bgnd.show_grid())
                    elif type == 4:
                        chk = powerup.check_coll(paddle, ball)
                    elif type == 5:
                        chk = powerup.check_coll(paddle)
                    if not chk:
                        powerups.remove(powerup)
                    powerup.erase_pow(bgnd.show_grid())
            elif stat == 1:
                sttime = powerup.get_sttime()
                os.system("aplay music/powerup.wav -q &")
                if type == 1:
                    if ref != 0.05:
                        ref = 0.05
                if type == 5:
                    if gap - pressed> 2:
                        stuck = True
                    if inp == 'p':
                        pressed = gap
                        stuck = False
                if curtime - sttime >= 15:
                    powerup.set_active(-1)
                    
            elif stat == -1:
                if type == 1:
                    ref = 0.1
                elif type == 2:
                    powerup.reset_pow(paddle,bgnd.show_grid())
                elif type == 3:
                    powerup.reset_pow(paddle,bgnd.show_grid())
                elif type == 4:
                    powerup.reset_pow(ball)
                elif type == 5:
                    stuck = False
                powerups.remove(powerup)
        os.system("clear")
        print("\033[%d;%dH" % (0, 0))
        #print(ball.get_x())
        #print(stat)
        print(bgnd.get_element(ball.get_x(),ball.get_y()))
        #print(paddle.get_y(), paddle.get_x())
        print(Fore.WHITE)
        print(Back.MAGENTA + "Time:", (round(time.time()) - round(strtime)), ' ', end="\t\t\t\t")
        print(Back.MAGENTA + "Lives: ",LIVES, end="\t\t\t\t")
        print(Back.MAGENTA + "Score: ",SCORE, end="\t\t\t\t")
        print(Back.MAGENTA + "Level: ",level, end="")
        print()
        print(Back.MAGENTA + "Powerups: ", movedto)
        print(RESET)
        '''for i in range(3,4):
            print(bgnd.get_element(10,5))'''
        #sys.stdout.write("\033c")
        bgnd.print_grid()
        
       


            