import curses, sys
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

    # Getting initial snake's length from the arguments
    try:
        snake_length = int(sys.argv[1]) if len(sys.argv) > 1 else 4

    except ValueError:
        snake_length = 4

    if snake_length > screen_width // 2:
        snake_length = screen_width // 2

    # Creating the box in which the player will be able to move
    textpad.rectangle(
        stdscr,
        rect_top_left[Y],
        rect_top_left[X],
        rect_bottom_right[Y],
        rect_bottom_right[X]
    )

    # Creating the snake (first parameter is the length)
    snake = Snake(
        snake_length,
        screen_height,
        screen_width,
        (HORIZONTAL, VELOCITY)
    )

    new_head = list()

    # Initializing the food
    food = Food(
        rect_top_left[Y],
        rect_top_left[X],
        rect_bottom_right[Y],
        rect_bottom_right[X]
    )

    erased = [0, 0]

    food.create_and_draw(stdscr, snake.body, erased)

    stdscr.addstr(0, 0, "Dev: Martin Nieva")

    for body_part in snake.body:
        stdscr.addch(body_part[Y], body_part[X], "#")

    stdscr.addstr(2, rect_top_left[X], "Length of your snake: ") # UI element

    stdscr.addstr(screen_height - 1, screen_width // 2 - len("Press ESC to quit") // 2, "Press ESC to quit") # UI element

    while True:
        key = stdscr.getch()

        # If statements for movement
        if key == curses.KEY_RIGHT and snake.direction != (HORIZONTAL, -VELOCITY):
            snake.direction = (HORIZONTAL, VELOCITY)

        elif key == curses.KEY_LEFT and snake.direction != (HORIZONTAL, VELOCITY):
            snake.direction = (HORIZONTAL, -VELOCITY)

        elif key == curses.KEY_DOWN and snake.direction != (VERTICAL, -VELOCITY):
            snake.direction = (VERTICAL, VELOCITY)

        elif key == curses.KEY_UP and snake.direction != (VERTICAL, VELOCITY):
            snake.direction = (VERTICAL, -VELOCITY)

        elif key == 27: # If player presses ESC, then quit
            break

        position, delta = snake.direction

        new_head = snake.body[HEAD].copy()
        new_head[position] += delta

        # Make the player quit if he touches the walls
        if new_head[Y] == rect_top_left[Y] or new_head[Y] == rect_bottom_right[Y]:
            break

        elif new_head[X] == rect_top_left[X] or new_head[X] == rect_bottom_right[X]:
            break

        # Make the player's length increment if he touches the drawn food
        if new_head[Y] == food.y and new_head[X] == food.x:
            snake.length += 1
            food.create_and_draw(stdscr, snake.body, erased)

        # Make the player quit if he touches himself
        if new_head in snake.body:
            break

        snake.body.insert(0, new_head)

        stdscr.addch(snake.body[HEAD][Y], snake.body[HEAD][X], "#")
        stdscr.addch(snake.body[TAIL][Y], snake.body[TAIL][X], " ")

        if len(snake.body) > snake.length:
            erased = snake.body.pop()

        snake_length_digits = len(list(str(snake.length)))

        stdscr.addstr(2, rect_bottom_right[X] - (snake_length_digits - 1), "{}".format(snake.length))

        # stdscr.addstr(screen_height - 6, 5, "{}".format(snake.body))
        # stdscr.addstr(screen_height - 1, 5, "{} {}".format(food.y, food.x))

curses.wrapper(main)
