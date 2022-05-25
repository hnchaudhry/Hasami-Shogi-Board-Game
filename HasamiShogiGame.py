# Author: Hassan Chaudhry
# Date: 12/3/2021
# Description: A program that defines a class called HasamiShogiGame that is used to play a variant of Hasami Shogi
#              between two players where one player has 9 black pieces and the other player has 9 red pieces. The goal
#              of the game is to alternate turns moving around a 9x9 board and capturing the other players' pieces.
#              Once one color has only one or no pieces left, then the other color is declared the winner of the game.

class HasamiShogiGame:
    """
    A class that represents a Hasami Shogi game. It is a game with a 9x9 board, and each player has 9 pieces that are
    either black or red. The player with the black pieces goes first and moves are alternated between the players. Red
    pieces start at the top of the board and the black pieces start at the bottom. Moves must only be vertical or
    horizontal without jumping over other pieces. Pieces are captured when the active player occupies two adjacent
    (vertically or horizontally) squares to the enemy player's piece. Multiple pieces can be captured if all squares
    between the active player's pieces contain enemy pieces. Corner captures happen when two of the active player's
    pieces orthogonally surround an enemy player's piece at a corner on the board. The game is won when one color
    has only one or no pieces left on the board.
    """
    def __init__(self):
        """
        Constructor for HasamiShogiGame class. Takes no parameters and initializes private data members for game state,
        active player, number of black pieces captured, number of red pieces captured, 2D array game board, a dictionary
        for corresponding algebraic notation squares (keys) to indices (values) in the board array, and a dictionary for
        corresponding algebraic notation squares (keys) that are corner capture locations to the orthogonal algebraic
        notation square and the algebraic notation of the corner square itself (values).
        """
        self._game_state = 'UNFINISHED'
        self._active_player = 'BLACK'
        self._black_num_captured_pieces = 0
        self._red_num_captured_pieces = 0
        self._board = [[' ', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                       ['a', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
                       ['b', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['c', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['d', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['e', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['f', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['g', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['h', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['i', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
        self._board_moves = {'a1': [1, 1], 'a2': [1, 2], 'a3': [1, 3], 'a4': [1, 4], 'a5': [1, 5], 'a6': [1, 6],
                             'a7': [1, 7], 'a8': [1, 8], 'a9': [1, 9], 'b1': [2, 1], 'b2': [2, 2], 'b3': [2, 3],
                             'b4': [2, 4], 'b5': [2, 5], 'b6': [2, 6], 'b7': [2, 7], 'b8': [2, 8], 'b9': [2, 9],
                             'c1': [3, 1], 'c2': [3, 2], 'c3': [3, 3], 'c4': [3, 4], 'c5': [3, 5], 'c6': [3, 6],
                             'c7': [3, 7], 'c8': [3, 8], 'c9': [3, 9], 'd1': [4, 1], 'd2': [4, 2], 'd3': [4, 3],
                             'd4': [4, 4], 'd5': [4, 5], 'd6': [4, 6], 'd7': [4, 7], 'd8': [4, 8], 'd9': [4, 9],
                             'e1': [5, 1], 'e2': [5, 2], 'e3': [5, 3], 'e4': [5, 4], 'e5': [5, 5], 'e6': [5, 6],
                             'e7': [5, 7], 'e8': [5, 8], 'e9': [5, 9], 'f1': [6, 1], 'f2': [6, 2], 'f3': [6, 3],
                             'f4': [6, 4], 'f5': [6, 5], 'f6': [6, 6], 'f7': [6, 7], 'f8': [6, 8], 'f9': [6, 9],
                             'g1': [7, 1], 'g2': [7, 2], 'g3': [7, 3], 'g4': [7, 4], 'g5': [7, 5], 'g6': [7, 6],
                             'g7': [7, 7], 'g8': [7, 8], 'g9': [7, 9], 'h1': [8, 1], 'h2': [8, 2], 'h3': [8, 3],
                             'h4': [8, 4], 'h5': [8, 5], 'h6': [8, 6], 'h7': [8, 7], 'h8': [8, 8], 'h9': [8, 9],
                             'i1': [9, 1], 'i2': [9, 2], 'i3': [9, 3], 'i4': [9, 4], 'i5': [9, 5], 'i6': [9, 6],
                             'i7': [9, 7], 'i8': [9, 8], 'i9': [9, 9]}
        self._corner_captures = {'b1': ['a2', 'a1'], 'a2': ['b1', 'a1'], 'b9': ['a8', 'a9'], 'a8': ['b9', 'a9'],
                                 'h1': ['i2', 'i1'], 'i2': ['h1', 'i1'], 'h9': ['i8', 'i9'], 'i8': ['h9', 'i9']}

    def get_game_state(self):
        """
        Takes no parameters and returns the current game state. The game state may be 'UNFINISHED', 'RED_WON',
        or 'BLACK_WON'.
        """
        return self._game_state

    def get_active_player(self):
        """
        Takes no parameters and returns the current active player. The active player may be 'BLACK' or 'RED'.
        """
        return self._active_player

    def get_num_captured_pieces(self, color_str):
        """
        Takes as a parameter a color string being either 'BLACK' or 'RED' and returns the number of captured
        pieces of the specified color.
        """
        if color_str == 'BLACK':
            return self._black_num_captured_pieces
        elif color_str == 'RED':
            return self._red_num_captured_pieces
        else:
            return

    def make_move(self, from_square_str, to_square_str):
        """
        Takes as parameters two strings (in algebraic notation e.g. 'a3') representing squares on the board with the
        first string being a location the active player would like to move a piece from and the second string being
        the location they would like to move the piece to. Uses validate_move method to validate moving the piece.
        If validate_move returns True, it uses the check_captures method to check if the valid move resulted in any
        enemy pieces being captured. It then updates the game state according to the number of captured pieces for
        each color, updates the active player to the other color, and returns True. If the move was not valid, it
        returns False.
        """
        # Retrieve indices of from and to squares from moves dictionary
        move_from_index = self._board_moves.get(from_square_str)
        move_to_index = self._board_moves.get(to_square_str)

        # Squares not in dict then return False otherwise set row and col indices
        if move_from_index is None or move_to_index is None:
            return False
        else:
            from_row = move_from_index[0]
            from_col = move_from_index[1]
            to_row = move_to_index[0]
            to_col = move_to_index[1]

        move_validation = self.validate_move(from_row, from_col, to_row, to_col)  # Will be True or False

        # Validate move is False then return False otherwise call check captures method
        if move_validation is False:
            return False
        else:
            self.check_captures(to_row, to_col, to_square_str)

        # Check number of captured pieces of each color and set game state accordingly
        if self._black_num_captured_pieces == 8 or self._black_num_captured_pieces == 9:
            self._game_state = 'RED_WON'
        elif self._red_num_captured_pieces == 8 or self._red_num_captured_pieces == 9:
            self._game_state = 'BLACK_WON'

        # Set new active player
        if self._active_player == 'BLACK':
            self._active_player = 'RED'
        else:
            self._active_player = 'BLACK'

        return True

    def validate_move(self, from_row, from_col, to_row, to_col):
        """
        Takes as parameters from row index, from column index, to row index, and to column index. Returns False if
        the piece being moved does not belong to the active player, or the move is not legal, or the game is already
        won. Returns True if the piece does belong to the active player, the move is legal, and the game is unfinished.
        Used by the make_move method.
        """
        moving_piece = self._board[from_row][from_col]  # The occupant of from square

        # Return False: not active player, game already won, not horizontal/vertical move, piece doesn't move
        if moving_piece != self._active_player[0]:
            return False
        elif self._game_state == 'BLACK_WON' or self._game_state == 'RED_WON':
            return False
        elif from_row != to_row and from_col != to_col:
            return False
        elif from_row == to_row and from_col == to_col:
            return False
        else:
            # Check horizontal move doesn't have pieces in the way
            if from_row == to_row and from_col != to_col:
                # Horizontal right move
                if to_col > from_col:
                    from_col_copy = from_col
                    from_col += 1
                    while from_col <= to_col:
                        if self._board[to_row][from_col] != '.':
                            return False
                        else:
                            from_col += 1
                    self._board[to_row][to_col] = moving_piece
                    self._board[from_row][from_col_copy] = '.'
                    return True

                # Horizontal left move
                else:
                    from_col_copy = from_col
                    from_col -= 1
                    while from_col >= to_col:
                        if self._board[to_row][from_col] != '.':
                            return False
                        else:
                            from_col -= 1
                    self._board[to_row][to_col] = moving_piece
                    self._board[from_row][from_col_copy] = '.'
                    return True

            # Check vertical move doesn't have pieces in the way
            else:
                # Vertical down move
                if to_row > from_row:
                    from_row_copy = from_row
                    from_row += 1
                    while from_row <= to_row:
                        if self._board[from_row][to_col] != '.':
                            return False
                        else:
                            from_row += 1
                    self._board[to_row][to_col] = moving_piece
                    self._board[from_row_copy][from_col] = '.'
                    return True

                # Vertical up move
                else:
                    from_row_copy = from_row
                    from_row -= 1
                    while from_row >= to_row:
                        if self._board[from_row][to_col] != '.':
                            return False
                        else:
                            from_row -= 1
                    self._board[to_row][to_col] = moving_piece
                    self._board[from_row_copy][from_col] = '.'
                    return True

    def check_captures(self, to_row, to_col, to_square_str):
        """
        Takes as parameters to row index, to column index, and the algebraic notation string of the to square. It
        checks to see if a valid move would result in any enemy pieces being captured and updates number of pieces
        captured accordingly. Used by the make_move method.
        """
        # Check for corner capture
        if to_square_str in self._corner_captures:
            corner_capture_list = self._corner_captures.get(to_square_str)
            corresponding_square_color = self.get_square_occupant(corner_capture_list[0])
            corner_square_color = self.get_square_occupant(corner_capture_list[1])
            if corresponding_square_color[0] == self._active_player[0]:
                if corner_square_color != '.' and corner_square_color != self._active_player[0]:
                    if corner_square_color[0] == 'R':
                        self._red_num_captured_pieces += 1
                        self.set_square_occupant(corner_capture_list[1], '.')
                    elif corner_square_color[0] == 'B':
                        self._black_num_captured_pieces += 1
                        self.set_square_occupant(corner_capture_list[1], '.')

        # Copies of to row and to column indices
        to_row_up = to_row
        to_row_down = to_row
        to_col_right = to_col
        to_col_left = to_col

        # Check if valid move led to capture in vertical up direction
        capture_counter = 0
        to_row_up -= 1
        if to_row_up > 0 and self._board[to_row_up][to_col] != self._active_player[0] and \
                self._board[to_row_up][to_col] != '.':
            while to_row_up > 0 and self._board[to_row_up][to_col] != self._active_player[0] and \
                    self._board[to_row_up][to_col] != '.':
                capture_counter += 1
                to_row_up -= 1
            if to_row_up > 0 and self._board[to_row_up][to_col] == self._active_player[0]:
                if self._active_player[0] == 'B':
                    self._red_num_captured_pieces += capture_counter
                elif self._active_player[0] == 'R':
                    self._black_num_captured_pieces += capture_counter
                for num in range(0, capture_counter):
                    to_row_up += 1
                    self._board[to_row_up][to_col] = '.'

        # Check if valid move led to capture in vertical down direction
        capture_counter = 0
        to_row_down += 1
        if to_row_down < 10 and self._board[to_row_down][to_col] != self._active_player[0] and \
                self._board[to_row_down][to_col] != '.':
            while to_row_down < 10 and self._board[to_row_down][to_col] != self._active_player[0] and \
                    self._board[to_row_down][to_col] != '.':
                capture_counter += 1
                to_row_down += 1
            if to_row_down < 10 and self._board[to_row_down][to_col] == self._active_player[0]:
                if self._active_player[0] == 'B':
                    self._red_num_captured_pieces += capture_counter
                elif self._active_player[0] == 'R':
                    self._black_num_captured_pieces += capture_counter
                for num in range(0, capture_counter):
                    to_row_down -= 1
                    self._board[to_row_down][to_col] = '.'

        # Check if valid move led to capture in horizontal right direction
        capture_counter = 0
        to_col_right += 1
        if to_col_right < 10 and self._board[to_row][to_col_right] != self._active_player[0] and \
                self._board[to_row][to_col_right] != '.':
            while to_col_right < 10 and self._board[to_row][to_col_right] != self._active_player[0] and \
                    self._board[to_row][to_col_right] != '.':
                capture_counter += 1
                to_col_right += 1
            if to_col_right < 10 and self._board[to_row][to_col_right] == self._active_player[0]:
                if self._active_player[0] == 'B':
                    self._red_num_captured_pieces += capture_counter
                elif self._active_player[0] == 'R':
                    self._black_num_captured_pieces += capture_counter
                for num in range(0, capture_counter):
                    to_col_right -= 1
                    self._board[to_row][to_col_right] = '.'

        # Check if valid move led to capture in horizontal left direction
        capture_counter = 0
        to_col_left -= 1
        if to_col_left > 0 and self._board[to_row][to_col_left] != self._active_player[0] and \
                self._board[to_row][to_col_left] != '.':
            while to_col_left > 0 and self._board[to_row][to_col_left] != self._active_player[0] and \
                    self._board[to_row][to_col_left] != '.':
                capture_counter += 1
                to_col_left -= 1
            if to_col_left > 0 and self._board[to_row][to_col_left] == self._active_player[0]:
                if self._active_player[0] == 'B':
                    self._red_num_captured_pieces += capture_counter
                elif self._active_player[0] == 'R':
                    self._black_num_captured_pieces += capture_counter
                for num in range(0, capture_counter):
                    to_col_left += 1
                    self._board[to_row][to_col_left] = '.'

    def get_square_occupant(self, square_str):
        """
        Takes as a parameter an algebraic notation string of a square on the game board and returns the occupant
        of the square. The occupant may be 'BLACK', 'RED', or 'None' if the square is empty. Used by the check_captures
        method.
        """
        square_index = self._board_moves.get(square_str)
        row = square_index[0]
        col = square_index[1]
        occupant = self._board[row][col]
        if occupant == 'B':
            return 'BLACK'
        elif occupant == 'R':
            return 'RED'
        else:
            return 'NONE'

    def set_square_occupant(self, square_str, new_occupant_str):
        """
        Takes as parameters an algebraic notation string of a square on the board and a string for a new occupant.
        It will update the square with the specified new occupant. Used by the check_captures method.
        """
        square_index = self._board_moves.get(square_str)
        row = square_index[0]
        col = square_index[1]
        self._board[row][col] = new_occupant_str

    def print_board(self):
        """
        Takes no parameters and prints out a formatted version of the 2D array game board in its current state.
        """
        for rows in self._board:
            for cols in rows:
                print(cols, end=" ")
            print()
