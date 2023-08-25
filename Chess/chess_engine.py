"""
Responsible to store information of current state of the game.
Also responsible for determining valid moves. Also keep a move log.
"""


class GameState:
    def __init__(self):
        # Declaring the board in the form of 2 dimensional lists. 8x8 2dimensional list
        # TODO --> Can be made efficient with help of numpy arrays
        # "--" empty square with no piece
        self.board = [
            ['bR', 'bN', 'bB', 'bK', 'bQ', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR'],
        ]

        # Variable to decide player turn
        self.white_to_move = True

        # Storing the moves in the move_log variable
        self.move_log = []

    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)  # Log the move
        self.white_to_move = not self.white_to_move  # switch the turns after a move


"""
Move class

"""


class Move:

    # Maps for chess notations
    # key: value

    # ranks and rows
    ranks_to_rows = {'1': 7, '2': 6, '3': 5, '4': 4,
                     '5': 3, '6': 2, '7': 1, '8': 0}
    rows_to_ranks = {value: key for key, value in ranks_to_rows.items()}

    # files and columns
    files_to_columns = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                        'e': 4, 'f': 5, 'g': 6, 'h': 7}
    columns_to_files = {value: key for key, value in files_to_columns.items()}

    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]

        # Piece data
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

    def get_chess_notation(self):
        # TODO --> Add real chess notation
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, row, col):
        return self.columns_to_files[col] + self.rows_to_ranks[row]
