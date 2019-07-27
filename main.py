import curses
from curses import textpad
from constants import *
from snake import *
from food import *

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1000 // FPS)

    screen_height, screen_width = stdscr.getmaxyx()

    rect_top_left = (3, screen_width // 3)
    rect_bottom_right = (screen_height - 3, (screen_width // 3) * 2)

    textpad.rectangle(
        stdscr, 
        rect_top_left[Y], 
        rect_top_left[X], 
        rect_bottom_right[Y], 
        rect_bottom_right[X]
    )

    snake = Snake(
        4, 
        screen_height, 
        screen_width, 
        (HORIZONTAL, VELOCITY)
    )

    food = Food(
        rect_top_left[Y], 
        rect_top_left[X], 
        rect_bottom_right[Y], 
        rect_bottom_right[X]
    )

    food.create_and_draw(stdscr, snake.body)

    new_head = list()

    for body_part in snake.body:
        stdscr.addch(body_part[Y], body_part[X], "#")

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

        if new_head[Y] == rect_top_left[Y] or new_head[Y] == rect_bottom_right[Y]:
            break

        elif new_head[X] == rect_top_left[X] or new_head[X] == rect_bottom_right[X]:
            break
   
        if new_head in snake.body:
            break

        if new_head[Y] == food.y and new_head[X] == food.x:
            snake.length += 1
            food.create_and_draw(stdscr, snake.body)

        snake.body.insert(0, new_head)

        stdscr.addch(snake.body[HEAD][Y], snake.body[HEAD][X], "#")
        stdscr.addch(snake.body[TAIL][Y], snake.body[TAIL][X], " ")
        
        if len(snake.body) > snake.length:
            snake.body.pop()

curses.wrapper(main)
