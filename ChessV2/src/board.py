# Imports
from const import *
from square import Square


class Board:

    # NOTE(To self): '_' at the function/ method is used to symbolise private functions
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0]
                        for col in range(COLS)]  # the Board

        self._create()

    '''This method generates the placeholders for pieces on the grid pattern'''

    def _create(self):

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        pass
