import pygame
from const import *
from board import Board

"""
This file handles the graphics of the game.
It is responsible for the rendering part of the game, e.g. the background.
"""


class Game:

    def __init__(self):
        self.board = Board()

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

    '''This method is responsible for rendering the pieces on the board'''
    def show_pieces(self, surface):
        
        # Looping through the board
        for row in range(ROWS):
            for col in range(COLS):
                # Checking for piece
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img  = pygame.image.load(piece.texture)
                    #  centering the image to the grid square
                    img_center = col*SQ_SIZE + SQ_SIZE//2, row*SQ_SIZE + SQ_SIZE//2
                    piece.texture_rect = img.get_rect(center=img_center)

                    surface.blit(img, piece.texture_rect)