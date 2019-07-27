import curses
from constants import *
from snake import *
from curses import textpad

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1000 // FPS)

    screen_height, screen_width = stdscr.getmaxyx()

    snake = Snake(3, screen_height, screen_width, (HORIZONTAL, VELOCITY))

    new_head = list()

    for body_part in snake.body:
        stdscr.addch(body_part[Y], body_part[X], "#")

    textpad.rectangle(stdscr, 3, 3, screen_height - 3, screen_width - 3)

    while True:
        key = stdscr.getch() 

        if key == curses.KEY_RIGHT:
            snake.direction = (HORIZONTAL, VELOCITY)

        elif key == curses.KEY_LEFT:
            snake.direction = (HORIZONTAL, -VELOCITY)

        elif key == curses.KEY_DOWN:
            snake.direction = (VERTICAL, VELOCITY)

        elif key == curses.KEY_UP:
            snake.direction = (VERTICAL, -VELOCITY)

        position, delta = snake.direction

        new_head = snake.body[HEAD].copy()
        new_head[position] += delta

        snake.body.insert(0, new_head)

        stdscr.addch(snake.body[HEAD][Y], snake.body[HEAD][X], "#")
        stdscr.addch(snake.body[TAIL][Y], snake.body[TAIL][X], " ")
        
        snake.body.pop()

curses.wrapper(main)
