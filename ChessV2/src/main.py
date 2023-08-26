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

        self.game = Game()

    def main_loop(self):

        screen = self.screen
        game = self.game

        running = True
        while running:

            # Drawing the grid pattern
            game.show_background(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.main_loop()
