# Imports
from const import *
from piece import *
from move import Move
from square import Square


class Board:

    # NOTE(To self): '_' at the function/ method is used to symbolise private functions
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0]
                        for col in range(COLS)]  # the Board

        self._create()
        self._add_pieces('white')  # adding white pieces
        self._add_pieces('black')  # adding black pieces

    '''Calculate all the possible moves for a piece on a position'''

    def calc_moves(self, piece, row, col):

        def pawn_moves():
            steps = 1 if piece.moved else 2

            # vertical moves
            start = row + piece.direction
            end = row + (piece.direction*(1+steps))
            for possible_move_row in range(start, end, piece.direction):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():

                        # creating squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)

                        # creataing moves
                        move = Move(initial, final)
                        # appending move
                        piece.add_move(move)
                    else:  # blocked
                        break
                else:  # not in range
                    break

            # diagonal moves (attacking)

            possible_move_row = row + piece.direction
            possible_move_cols = [col-1, col+1]  # left and right

            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):

                        # creating squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)

                        # creating moves
                        move = Move(initial, final)
                        # appending the move
                        piece.add_move(move)

        def knight_moves():
            # 8 possible moves for knight
            possible_moves = [
                (row-2, col+1),
                (row-2, col-1),
                (row-1, col+2),
                (row-1, col-2),
                (row+1, col+2),
                (row+1, col-2),
                (row+2, col+1),
                (row+2, col-1)
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(
                            piece.color):

                        # create squares for the move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)

                        # create new move for the piece
                        move = Move(initial, final)
                        # appending new valid move
                        piece.add_move(move)

        def bishop_moves():
            pass

        def rook_moves():
            pass

        def queen_moves():
            pass

        def king_moves():
            pass

        if isinstance(piece, Pawn):
            pawn_moves()

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            bishop_moves()

        elif isinstance(piece, Rook):
            rook_moves()

        elif isinstance(piece, Queen):
            queen_moves()

        elif isinstance(piece, King):
            king_moves()

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
