"""
This file handles all the attributes of the pieces like the pawn, queen, etc.
"""

# Imports
import os

'''This is the parent class. Other classes inherit this class'''
class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):

        self.name = name
        self.color = color

        # Giving values to the pieces for generating an AI
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign

        self.moves = []
        self.moved = False
        
        # Setting the images for the pieces
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    '''Image of the Piece'''

    def set_texture(self, size=80):

        # Locating the path to the images
        self.texture = os.path.join(
            f'C:\\Users\\Yash\\Desktop\\Chess-Python\\ChessV2\\assets\\images\\imgs-{size}px\\{self.color}_{self.name}.png'
        )

    def add_moves(self, move):
        self.moves.append(move)


'''This class is resonsible for the attributes of the pawn piece'''
class Pawn(Piece):

    def __init__(self, color):

        # Pawns can only move in a single direction
        self.direction = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)


'''This class is resonsible for the attributes of the knight piece'''
class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)


'''This class is resonsible for the attributes of the Bishop piece'''
class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.01)


'''This class is resonsible for the attributes of the rook piece'''
class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)


'''This class is resonsible for the attributes of the queen piece'''
class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0)


'''This class is resonsible for the attributes of the king piece'''
class King(Piece):

    def __init__(self, color):
        # an extremely high value is given to avoid capture of the king (only checks and checkmates)
        super().__init__('king', color, 1000.0)
