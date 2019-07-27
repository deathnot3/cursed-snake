import curses
from curses import textpad

def main(stdscr):
    curses.curs_set(0)

    screen_height, screen_width = stdscr.getmaxyx()

    snake_length = 3

    snake_body = [
        [screen_height // 2, screen_width // 2],
        [screen_height // 2, screen_width // 2 - 1],
        [screen_height // 2, screen_width // 2 - 2],
        [screen_height // 2, screen_width // 2 - 3]
    ]

    new_head = list()

    for body_part in snake_body:
        stdscr.addch(body_part[0], body_part[1], "#")

    while True:
        key = stdscr.getch() 

        if key == curses.KEY_RIGHT:
            new_head = [snake_body[0][0], snake_body[0][1] + 1]

        elif key == curses.KEY_LEFT:
            new_head = [snake_body[0][0], snake_body[0][1] - 1]

        elif key == curses.KEY_DOWN:
            new_head = [snake_body[0][0] + 1, snake_body[0][1]]

        elif key == curses.KEY_UP:
            new_head = [snake_body[0][0] - 1, snake_body[0][1]]
        
        snake_body.insert(0, new_head)

        stdscr.addch(snake_body[0][0], snake_body[0][1], "#")

        stdscr.addch(snake_body[-1][0], snake_body[-1][1], " ")
        
        snake_body.pop()

curses.wrapper(main)
