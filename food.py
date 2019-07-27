from random import randint

class Food:
    def __init__(self, min_y, min_x, max_y, max_x):
        self.min_y = min_y
        self.min_x = min_x
        
        self.max_y = max_y
        self.max_x = max_x

    def create_and_draw(self, stdscr, snake_body):
        flag = False

        while True:
            self.y = randint(self.min_y + 1, self.max_y - 1)
            self.x = randint(self.min_x + 1, self.max_x - 1)

            for body_part in snake_body:
                if self.x in body_part and self.y in body_part:
                    flag = True
                    break

            if flag == False:
                break

        stdscr.addch(self.y, self.x, "O")
