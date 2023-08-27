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
        dragger = self.game.dragger
        board = self.game.board

        # Initialising the main loop for the game
        running = True
        while running:

            # Drawing the grid pattern
            game.show_background(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            # Handling events that take place during the game
            for event in pygame.event.get():

                '''Adding a dragging event'''
                if event.type == pygame.MOUSEBUTTONDOWN:  # clicking on the piece
                    dragger.update_mouse(event.pos)

                    #  checking piece for piece in the position
                    clicked_row = dragger.mouse_y // SQ_SIZE
                    clicked_col = dragger.mouse_x // SQ_SIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece

                        board.calc_moves(piece, clicked_row, clicked_col)

                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                        # Show methods
                        game.show_background(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)

                elif event.type == pygame.MOUSEMOTION:  # the motion of cursor after click
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        
                        # to prevent trailing image of the dragged piece
                        game.show_background(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        
                        dragger.update_blit(screen)

                elif event.type == pygame.MOUSEBUTTONUP:  # after releasing the mouse click
                    dragger.undrag_piece()

                # Quitting the application
                elif event.type == pygame.QUIT:
                    running = False

            pygame.display.update()


if __name__ == "__main__":
    main = Main()
    main.main_loop()
