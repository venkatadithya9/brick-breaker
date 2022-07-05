import numpy as np
from header import *

class Ball:
    def __init__(self,x,y, xvel):
        self.__x = x
        self.__y = y
        self.__xvel = xvel
        self.__yvel = -1
        self.__thru = False
        self.__debug = 0
        self.__stick = False
       

    def print_ball(self,grid):
        x = self.__x
        y = self.__y
        #grid[y, x-1:x+1] = self.__body
        
        grid[y][x] = RED+'o'+RESET
        
    
    def erase_ball(self,grid):
        x = self.__x
        y = self.__y
        
        grid[y][x] = ' '
        
    
    def set_xvel(self, xvel):
        self.__xvel = xvel
        if self.__xvel >= 3:
            self.__xvel = 2

    def set_yvel(self, yvel):
        self.__yvel = yvel

    def set_thru(self, thru):
        self.__thru = thru

    def set_stick(self, stick):
        self.__stick = stick

    def get_xvel(self):
        return self.__xvel

    def get_yvel(self):
        return self.__yvel
    
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
    def get_thru(self):
        return self.__thru
    
    def get_stick(self):
        return self.__stick

    def get_debug(self):
        return self.__debug

    def set_pos(self, x, y, grid):
        self.erase_ball(grid)
        self.__x = x
        self.__y = y
        self.print_ball(grid)
    
    def check_edgecoll(self, grid, newx, newy):
        #print("inside edgecoll")
        
        if newx <= 3:
            self.__xvel = 0 - self.__xvel
        elif newx >= WIDTH-3:
            self.__xvel = 0 - self.__xvel
        if newy <= 3:
            self.__yvel = 0 - self.__yvel
    
    def check_paddlecoll(self, newx, newy,paddle):
        #print("inside paddle coll")
        x = paddle.get_x()
        vel = paddle.get_vel()
        len = paddle.get_len()
        if (len ==1 and newx < x+3 and newx> x-2) or (len != 1 and newx<=x+2 and newx >=x-1):
            return 0
        else:
            for i in range((int)(len/2)):
                if (newx >= (x+2+i*5) and newx < (x+2+(i+1)*5)) or (newx <= (x-1 -i*5) and newx > (x-1 -(i+1)*5)):
                    return vel*(i+1)
        return 100

    def path_manage(self,grid, paddle):
        
        #add check collision functions and then ball mechanics
        if self.__stick:
            pass
        else:
            self.erase_ball(grid)
            self.check_edgecoll(grid,self.__x,self.__y)
            self.__x = self.__x + self.__xvel
            self.__y = self.__y + self.__yvel
            self.print_ball(grid)
        #print(self.__y)
        #print(self.__x)

