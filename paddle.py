import numpy as np
from header import *

class Paddle:
    
    def __init__(self, vel) :
        self.__x = (int)(WIDTH/3)
        self.__y = HEIGHT - 8
        self.__length = 3
        self.__vel = vel
        self.__body3 = np.zeros((2,13), dtype='<U20')
        self.__body3[0] = [' ', CYAN+'_','_','_','_','_','_','_','_','_','_','_'+RESET,' ']
        self.__body3[1] = [CYAN+'(','_','_','_','|','_','_','_','|','_','_','_',')'+RESET]
        self.__body1 = np.zeros((2,5), dtype='<U20')
        self.__body1[0] = [' ', CYAN+'_','_','_'+RESET,' ']
        self.__body1[1] = [CYAN+'(','_','_','_',')'+RESET]
        self.__body5 = np.zeros((2,21), dtype='<U20')
        self.__body5[0] = [' ',CYAN+'_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'+RESET,' ']
        self.__body5[1] = [CYAN+'(','_','_','_','|','_','_','_','|','_','_','_','|','_','_','_','|','_','_','_',')'+RESET]
        self.__emp3 = np.zeros((2,13), dtype='<U20')
        self.__emp5 = np.zeros((2,21), dtype='<U20')
        self.__emp1 = np.zeros((2,5), dtype='<U20')
        self.__emp3[:] = ' '
        self.__emp5[:] = ' '
        self.__emp1[:] = ' '
        self.__body = np.zeros((2,5 + (self.__length - 1)*4), dtype='<U20')
        self.__emp = np.zeros((2,5 + (self.__length - 1)*4), dtype='<U20')
        self.__emp[:] = ' '
        self.__prevx = 0
        self.__prevy = 0

    def create_paddle(self):
        len = (self.__length - 1)*4 + 5
        temp = np.zeros((2, len), dtype='<U20')
        for i in range(len):
            if i ==0 or i==len-1:
                temp[0][i] = ' '
                temp[1][0] = CYAN+'('+RESET
                temp[1][len-1] = CYAN+')'+RESET
            elif i%4 == 0:
                temp[0][i] = CYAN+'_'+RESET
                temp[1][i] = CYAN+'|'+RESET
            else:
                temp[0][i] = CYAN+'_'+RESET
                temp[1][i] = CYAN+'_'+RESET
        self.__body = temp
            

    def print_paddle(self, grid):
        self.create_paddle()
        len = (int)((self.__length*4 + 1)/2)
        x = self.__x
        y = self.__y
        grid[y-1:y+1, x-len:x+len+1] = self.__body
    
    def erase_paddle(self, grid):
        len = (int)((self.__length*4 + 1)/2)
        temp = np.zeros((2,len*2 +1), dtype='<U20')
        temp[:] = ' '
        x = self.__x
        y = self.__y
        self.__emp = temp
        grid[y-1:y+1, x-len:x+len+1] = self.__emp
    
    def move_paddle(self, grid, dir):
        len = (int)((self.__length*4 + 1)/2)
        self.__vel = dir
        self.erase_paddle(grid)
        #print(self.__y)
        if dir == -1 and self.__x-len<=3:
            self.__x = self.__x
        elif dir == 1 and self.__x+len+1>=WIDTH:
            self.__x = self.__x
        else:
            self.__x = self.__x + dir
        #print(self.__x)
        self.print_paddle(grid)

    def set_vel(self, vel):
        self.__vel = vel
    
    def set_len(self, len):
        self.__length = len

    def get_vel(self):
        return self.__vel

    def get_len(self):
        return self.__length
    
    def get_xpos(self):
        return self.__x + self.__vel
    
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
           


