# Imports
from const import *
from piece import *
from square import Square


class Board:

    # NOTE(To self): '_' at the function/ method is used to symbolise private functions
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0]
                        for col in range(COLS)]  # the Board

        self._create()
        self._add_pieces('white')  # adding white pieces
        self._add_pieces('black')  # adding black pieces

    '''This method generates the placeholders for pieces on the grid pattern'''

    def _create(self):

        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):

        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # adding pawns (8 pawns)
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # adding knights (2 knights)
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # adding bishops (2 bishops)
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # adding rooks (2 rooks)
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # adding queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # adding king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
