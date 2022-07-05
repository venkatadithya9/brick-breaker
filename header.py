import os
from colorama import Fore, Back, init, Style
init()

rows, columns = os.popen('stty size', 'r').read().split()
HEIGHT = int(rows) - 7 
WIDTH = int(columns)
#print(WIDTH)

LIVES = 5
RESET = Style.RESET_ALL
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
CYAN = Fore.CYAN 
WHITE = Fore.WHITE
RED = Fore.RED
GCOLOR = Fore.LIGHTGREEN_EX+Back.GREEN
BLING = Fore.LIGHTYELLOW_EX
#print(rows, columns)

layout = [False]*470
layout1 = [False]*470
layout2 = [False]*470
layout3 = [False]*470
SCORE = 0

#print(layout)