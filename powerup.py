from paddle import Paddle
from header import *
import time
import numpy as np

class Powerup:
    def __init__(self,x, y):
        self._sttime = 0
        self._track = time.time()
        self._active = 0
        self._type = 0
        self._x = x
        self._y = y
    
    def print_pow(self, grid):
        x = self._x
        y = self._y
        grid[y][x] = BLING+'o'+RESET

    def erase_pow(self,grid):
        x = self._x
        y = self._y
        
        grid[y][x] = ' '
    
    def set_sttime(self, sttime):
        self._sttime = sttime
        self._active = 1
    
    def set_active(self, active):
        self._active = active
    
    def get_sttime(self):
        return self._sttime
    
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
    
    def get_active(self):
        return self._active
    
    def get_type(self):
        return self._type

    def move_pow(self, grid):
        self.erase_pow(grid)
        self._y += 2
        self.print_pow(grid)
    
    def check_coll(self, paddle):
        x = paddle.get_x()
        y = paddle.get_y()
        len = (int)((paddle.get_len()*4 + 1)/2)

        if self._x <= x+ len and self._x >= x-len:
            return True
        else:
            return False

class Speedball(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = 1
       
    def print_pow(self, grid):
        x = self._x
        y = self._y
        grid[y][x] = BLING + 'F' + RESET
    

    def check_coll(self, paddle):
        x = paddle.get_x()
        y = paddle.get_y()
        len = (int)((paddle.get_len()*4 + 1)/2)

        if self._x <= x+ len and self._x >= x-len:
            self.set_sttime(time.time())
            
            return True
        else:
            return False

class Expandpaddle(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = 2
       
    def print_pow(self, grid):
        x = self._x
        y = self._y
        grid[y][x] = BLING + 'E' + RESET
    
    
    def check_coll(self, paddle, grid):
        x = paddle.get_x()
        y = paddle.get_y()
        len = (int)((paddle.get_len()*4 + 1)/2)

        if self._x <= x+ len and self._x >= x-len:
            if self._active == 0:
                paddle.erase_paddle(grid)
                paddle.set_len(paddle.get_len() + 2)
                paddle.print_paddle(grid)
            self.set_sttime(time.time())
            
            return True
        else:
            return False
    
    def reset_pow(self,paddle, grid):
        paddle.erase_paddle(grid)
        paddle.set_len(paddle.get_len() - 2)
        paddle.print_paddle(grid)

class Shrinkpaddle(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = 3
       
    def print_pow(self, grid):
        x = self._x
        y = self._y
        grid[y][x] = BLING + 's' + RESET
    
    
    def check_coll(self, paddle, grid):
        x = paddle.get_x()
        y = paddle.get_y()
        len = (int)((paddle.get_len()*4 + 1)/2)

        if self._x <= x+ len and self._x >= x-len:
            if self._active == 0:
                paddle.erase_paddle(grid)
                paddle.set_len(paddle.get_len() - 2)
                paddle.print_paddle(grid)
            self.set_sttime(time.time())
            
            return True
        else:
            return False
    
    def reset_pow(self,paddle, grid):
        paddle.erase_paddle(grid)
        paddle.set_len(paddle.get_len() + 2)
        paddle.print_paddle(grid)

class Thruball(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = 4
       
    def print_pow(self, grid):
        x = self._x
        y = self._y
        grid[y][x] = BLING + 'T' + RESET
    
    
    def check_coll(self, paddle, ball):
        x = paddle.get_x()
        y = paddle.get_y()
        len = (int)((paddle.get_len()*4 + 1)/2)

        if self._x <= x+ len and self._x >= x-len:
            if self._active == 0:
                ball.set_thru(True)
            self.set_sttime(time.time())
            
            return True
        else:
            return False
    
    def reset_pow(self,ball):
        ball.set_thru(False)

class Paddlegrab(Powerup):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = 5
       
    def print_pow(self, grid):
        x = self._x
        y = self._y
        grid[y][x] = BLING + 'P' + RESET
    
    
    def check_coll(self, paddle):
        x = paddle.get_x()
        y = paddle.get_y()
        len = (int)((paddle.get_len()*4 + 1)/2)

        if self._x <= x+ len and self._x >= x-len:
            self.set_sttime(time.time())
            
            return True
        else:
            return False
    