"""
This is the main driver file.
This file is responsible for handling game events, calling other objects.
"""

# Imports
import pygame
from const import *  # const.py
from game import Game


class Main:

    def __init__(self):

        pygame.init()  # initialising the pygame module
        # screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess-Python')
        # initialising the Game class
        # This will help to render and hanlde the graphics of the game
        self.game = Game()

    '''This function calls other functions and methods and it responsible for running the game'''

    def main_loop(self):

        # Just for easier and cleaner code. This can be skipped
        screen = self.screen
        game = self.game

        # Initialising the main loop for the game
        running = True
        while running:

            # Drawing the grid pattern
            game.show_background(screen)
            game.show_pieces(screen)

            # Handling events that take place during the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.main_loop()
