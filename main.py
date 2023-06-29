import pygame
from pygame.locals import *
from board import Board
from maze_runner import MazeRunner

pygame.init()
DISPLAY = True
width=height = 640 # must be same size
window = pygame.display.set_mode((width, height))
window.fill((255, 255, 255))
import time

win = Board(width,height, window)
maze_runner_obj = MazeRunner(window)
board_size = [22, 22]
win.update_wall_status(0, 0, 0)
Done = False
while True:
    if DISPLAY:
        pygame.display.update()
    if win.done:
        pygame.display.update()
        print('finished')
        DISPLAY_BEFORE_DONE = True
        break
    win.draw_board()
    win.draw_maze_runner(maze_runner_obj)
    win.maze_runner_road(maze_runner_obj)

time.sleep(60)
