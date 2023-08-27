import pygame
from const import *


"""
This file handles the graphics of the game.
It is responsible for the rendering part of the game, e.g. the background.
"""


class Game:

    def __init__(self):
        pass

    '''This method is responsible for rendering the background of the chess board'''

    def show_background(self, surface):

        # Generating the grid pattern
        for row in range(ROWS):
            for col in range(COLS):
                if (row+col) % 2 == 0:
                    color = (234, 235, 200)  # light green
                else:
                    color = (119, 154, 88)  # dark green

                rect = (col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE)

                pygame.draw.rect(surface, color, rect)
