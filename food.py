from random import randint
from constants import *

class Food:
    def __init__(self, min_y, min_x, max_y, max_x):
        self.min_y = min_y
        self.min_x = min_x
        
        self.max_y = max_y
        self.max_x = max_x

    def create_and_draw(self, stdscr, snake_body, erased):
        flag = False

        self.y = randint(self.min_y + 1, self.max_y - 1)
        self.x = randint(self.min_x + 1, self.max_x - 1)

        while True:
            for body_part in snake_body:
                if self.x in body_part and self.y in body_part or self.y == erased[Y] and self.x == erased[X]:
                    flag = True
                    break
            
            else:
                flag = False
                break

            if flag:
                self.y = randint(self.min_y + 1, self.max_y - 1)
                self.x = randint(self.min_x + 1, self.max_x - 1)

        stdscr.addch(self.y, self.x, "O")
