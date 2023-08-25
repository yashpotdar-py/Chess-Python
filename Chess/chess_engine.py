"""
Responsible to store information of current state of the game.
Also responsible for determining valid moves. Also keep a move log.
"""


class GameState:
    def __init__(self):
        # Declaring the board in the form of 2 dimensional lists. 8x8 2dimensional list
        # Can be made efficient with help of numpy arrays
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
