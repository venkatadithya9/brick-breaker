from header import *
import numpy as np
import random

class Brick:
    def __init__(self, type, id):
        self.__id = id
        self.__x = 7 + 8*(id%22)
        self.__y = ((int)(id/22))*2 + 5
        self.__type = type
        self.__changes = random.randint(0, 10)
        if type != 0:
            self.__strength = type
        else:
            self.__strength = 100
        self.__body0 = np.zeros((2,8), dtype='<U20')
        self.__body0[0] = [' ',WHITE+'_','_','_','_','_','_'+RESET,' ']
        self.__body0[1] = [WHITE+'|','_','_','_','_','_','_','|'+RESET]
        self.__body1 = np.zeros((2,8), dtype='<U20')
        self.__body1[0] = [' ',GREEN+'_','_','_','_','_','_'+RESET,' ']
        self.__body1[1] = [GREEN+'|','_','_','_','_','_','_','|'+RESET]
        self.__body2 = np.zeros((2,8), dtype='<U20')
        self.__body2[0] = [' ',YELLOW+'_','_','_','_','_','_'+RESET,' ']
        self.__body2[1] = [YELLOW+'|','_','_','_','_','_','_','|'+RESET]
        self.__body3 = np.zeros((2,8), dtype='<U20')
        self.__body3[0] = [' ',BLUE+'_','_','_','_','_','_'+RESET,' ']
        self.__body3[1] = [BLUE+'|','_','_','_','_','_','_','|'+RESET]
        self.__body = np.zeros((2,8), dtype='<U20')
        self.__emp = np.zeros((2,8), dtype='<U20')
        self.__emp[:] = ' '
        if self.__type == 1:
            self.__body = self.__body1
            
        elif self.__type == 2:
            self.__body = self.__body2
            
        elif self.__type == 3:
            self.__body = self.__body3
        
        elif self.__type == 0:
            self.__body = self.__body0
            
        #layout[id] = True
    
    def print_brick(self, grid):
        #print("entered print brick")
        x = self.__x
        y = self.__y
        grid[y-1:y+1, x-4:x+4] = self.__body
    
    def erase_brick(self, grid):
        x = self.__x
        y = self.__y
        grid[y-1:y+1, x-4:x+4] = self.__emp
    
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
    def get_id(self):
        return self.__id
       
    def get_strength(self):
        return self.__strength

    def set_type(self, type):
        self.__type = type
    
    def set_id(self, id):
        self.__id = id
        self.__x = 7 + 8*(id%22)
        self.__y = ((int)(id/22))*2 + 5

    def set_y(self, y):
        self.__y = y


    def set_changes(self, changes):
        self.__changes = changes
    
    def check_coll(self, ball):
        if ball.get_x() in range(self.__x -5, self.__x + 5):
            if self.__strength > 0:
                x = self.__x
                y = self.__y
                if ((ball.get_x() == x+3 and ball.get_xvel() <0) or (ball.get_x() == x-4 and ball.get_xvel() > 0)) and (ball.get_y() == y or ball.get_y() == y-1):
                    ball.set_xvel(0 - ball.get_xvel()) 
                    return True
                elif (ball.get_y() == y and ball.get_yvel() < 0) or (ball.get_y() == y-1 and ball.get_yvel() > 0) and (ball.get_x() in range(x-4,x+4)):
                    ball.set_yvel(0 - ball.get_yvel())
                    return True
                else:   
                    return False

    def set_strength(self, ball):
        t = self.__type
        thru = ball.get_thru()
        if thru:
            self.__strength = 0
            return 1
        else:
            if self.__type == 0:
                return -1
            elif self.__strength > 1:
                self.__strength -= 1
                self.__type -= 1
                if t == 2:
                    self.__body = self.__body1
                else:
                    self.__body = self.__body2
                return 0
            else:
                self.__strength = 0
                return 1

    def change_colour(self):
        curstr = self.__strength + 1
        curtype = self.__type + 1
        if (self.__changes< 2 and self.__changes >= 0) and (self.__type != 0):
            if curstr == 2:
                self.__body = self.__body2
                self.__strength = curstr
                self.__type = curtype
            elif curstr == 3:
                self.__body = self.__body3
                self.__strength = curstr
                self.__type = curtype
            else:
                self.__body = self.__body1
                self.__type = 1
                self.__strength = 1
            