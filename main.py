import curses
from curses import textpad

def main(stdscr):
    curs_set(0)

curses.wrapper(stdscr)
