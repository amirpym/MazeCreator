import pygame
class MazeRunner:
    def __init__(self, window):
        self.coords = (0,0)
        self.previous_coords = (0,0)
        self.window = window


    def move(self, coords):
        self.previous_coords = self.coords
        self.coords = coords
