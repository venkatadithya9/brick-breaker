from header import *
import numpy as np

class Border:
    def __init__(self):
        self.__bottom = np.array([[Fore.LIGHTGREEN_EX+Back.LIGHTBLACK_EX + '-'+RESET, Fore.LIGHTGREEN_EX+Back.LIGHTBLACK_EX + '-'+RESET], [
                                      GCOLOR+'_'+RESET, GCOLOR+'^'+RESET], [GCOLOR+'_'+RESET, GCOLOR+'^'+RESET]])
        self.__top = np.array([[CYAN+'.'+RESET, CYAN+'\''+RESET], [
                                   CYAN+'\''+RESET, CYAN+'.'+RESET], [CYAN+'.'+RESET, CYAN+'\''+RESET]])

    def create_border(self, grid):
        if WIDTH%2 == 0:
            grid[HEIGHT-6:HEIGHT-3, 0:WIDTH] = np.tile(self.__bottom, (int)(WIDTH/2))
            
            grid[0:3, 0:WIDTH] = np.tile(self.__top, (int)(WIDTH/2))
        
        else:
            grid[HEIGHT-6:HEIGHT-3, 0:WIDTH-1] = np.tile(self.__bottom, (int)(WIDTH/2))
            
            grid[0:3, 0:WIDTH-1] = np.tile(self.__top, (int)(WIDTH/2))
