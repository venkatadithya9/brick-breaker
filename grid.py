import numpy as np
from header import *

class Grid:

    def __init__(self,rows,columns):

        self.__rows = rows
        self.__columns = columns
        self.__grid = np.zeros((HEIGHT, WIDTH), dtype='<U20')
        self.__grid[:] = ' '
        #self.__grid[HEIGHT-2][(int)(WIDTH/3)] = 'o'

    def print_grid(self):

        for i in range(self.__rows):
            for j in range(self.__columns):
                print("\033[1m" + self.__grid[i][j], end='')
            print()
    
    def show_grid(self):
        return self.__grid
    
    def get_element(self, x ,y):
        return self.__grid[y-7][x]
