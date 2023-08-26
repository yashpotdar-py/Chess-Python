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

        # Move functions
        self.move_funcions = {'p': self.get_pawn_moves,
                              'R': self.get_rook_moves,
                              'N': self.get_knight_moves,
                              'B': self.get_bishop_moves,
                              'Q': self.get_queen_moves,
                              'K': self.get_king_moves}

    """This will not work for castling, en-passant, and pawn promotion"""

    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)  # Log the move
        self.white_to_move = not self.white_to_move  # switch the turns after a move

    def undo_move(self):
        if len(self.move_log) != 0:  # making sure that there is a move to undo
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move  # switch turns back

    """All moves considering checks"""

    def get_valid_moves(self):
        return self.get_possible_moves()  # TODO Not worry about checks for now

    """All moves not considering checks"""

    def get_possible_moves(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0]  # checking whose turn it is
                if (turn == 'w' and self.white_to_move) or (
                        turn == 'b' and not self.white_to_move):
                    # checking for the piece type
                    piece = self.board[row][col][1]
                    self.move_funcions[piece](row, col, moves)
        return moves

    '''Get Pawn Moves'''

    def get_pawn_moves(self, row, col, moves):

        # white pawn
        if self.white_to_move:
            move_amount = -1  # since white pieces move up the grid
            start_row = 6
            enemy_color = 'b'
        # black pawn
        else:
            move_amount = 1  # since balck pieces move down the grid
            start_row = 1
            enemy_color = 'w'

        # 1 square pawn advance
        if self.board[row+move_amount][col] == "--":
            moves.append(Move((row, col), (row+move_amount, col), self.board))
            # 2 square pawn advance
            if row == start_row and self.board[row+(2*move_amount)][col] == "--":
                moves.append(
                    Move((row, col), (row+(2*move_amount), col), self.board))

        # capture to the left
        if col-1 >= 0:
            if self.board[row+move_amount][col-1][0] == enemy_color:
                moves.append(
                    Move((row, col), (row+move_amount, col-1), self.board))

        # capture to the right
        if col+1 <= 7:
            if self.board[row+move_amount][col+1][0] == enemy_color:
                moves.append(
                    Move((row, col), (row+move_amount, col+1), self.board))

    '''Get Rook Moves'''

    def get_rook_moves(self, row, col, moves):

        # up, left, down, right
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        enemy_color = "b" if self.white_to_move else "w"
        for direction in directions:
            for i in range(1, 8):
                end_row = row + direction[0] * i
                end_col = col + direction[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:  # check for possible moves only in boundaries of the board
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "--":  # empty space is valid
                        moves.append(
                            Move((row, col), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:  # capture enemy piece
                        moves.append(
                            Move((row, col), (end_row, end_col), self.board))
                        break
                    else:  # friendly piece
                        break
                else:  # off board
                    break

    '''Get Knight Moves'''

    def get_knight_moves(self, row, col, moves):
        # up/left up/right right/up right/down down/left down/right left/up left/down
        knight_moves = ((-2, -1), (-2, 1), (-1, 2), (1, 2),
                        (2, -1), (2, 1), (-1, -2), (1, -2))
        ally_color = "w" if self.white_to_move else "b"
        for move in knight_moves:
            end_row = row + move[0]
            end_col = col + move[1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                # so its either enemy piece or empty square
                if end_piece[0] != ally_color:
                    moves.append(
                        Move((row, col), (end_row, end_col), self.board))

    '''Get Bishop Moves'''

    def get_bishop_moves(self, row, col, moves):
        # diagonals: up/left up/right down/right down/left
        directions = ((-1, -1), (-1, 1), (1, 1), (1, -1))
        enemy_color = "b" if self.white_to_move else "w"
        for direction in directions:
            for i in range(1, 8):
                end_row = row + direction[0] * i
                end_col = col + direction[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:  # check if the move is on board
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "--":  # empty space is valid
                        moves.append(
                            Move((row, col), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:  # capture enemy piece
                        moves.append(
                            Move((row, col), (end_row, end_col), self.board))
                        break
                    else:  # friendly piece
                        break
                else:  # off board
                    break

    '''Get Queen Moves'''

    def get_queen_moves(self, row, col, moves):
        self.get_bishop_moves(row, col, moves)
        self.get_rook_moves(row, col, moves)

    '''Get King Moves'''

    def get_king_moves(self, row, col, moves):
        king_moves = ((-1, -1), (-1, 1), (1, 1), (1, -1),
                      (-1, 0), (0, -1), (1, 0), (0, 1))
        ally_color = 'w' if self.white_to_move else 'b'
        for i in range(8):
            end_row = row+king_moves[i][0]
            end_col = row+king_moves[i][1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece[0] != ally_color:
                    moves.append(
                        Move((row, col), (end_row, end_col), self.board))


"""Move class"""


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

        self.move_id = (self.start_row * 1000)
        + (self.start_col * 100)
        + (self.end_row * 10)
        + self.end_col

    '''Overiding an equals method'''

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_id == other.move_id
        return False

    def get_chess_notation(self):
        # TODO --> Add real chess notation
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, row, col):
        return self.columns_to_files[col] + self.rows_to_ranks[row]
