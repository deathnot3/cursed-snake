import curses
from snake import *
from curses import textpad

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1000 // 5)

    screen_height, screen_width = stdscr.getmaxyx()

    snake = Snake(3, screen_height, screen_width, (1, 1))

    new_head = list()

    for body_part in snake.body:
        stdscr.addch(body_part[0], body_part[1], "#")

    textpad.rectangle(stdscr, 3, 3, screen_height - 3, screen_width - 3)

    while True:
        key = stdscr.getch() 

        if key == curses.KEY_RIGHT:
            snake.direction = (1, 1)

        elif key == curses.KEY_LEFT:
            snake.direction = (1, -1)

        elif key == curses.KEY_DOWN:
            snake.direction = (0, 1)

        elif key == curses.KEY_UP:
            snake.direction = (0, -1)

        position, delta = snake.direction

        new_head = snake.body[0].copy()
        new_head[position] += delta

        snake.body.insert(0, new_head)

        stdscr.addch(snake.body[0][0], snake.body[0][1], "#")
        stdscr.addch(snake.body[-1][0], snake.body[-1][1], " ")
        
        snake.body.pop()

curses.wrapper(main)
