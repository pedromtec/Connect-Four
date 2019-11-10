class Board:
    ROWS = 6
    COLUMNS = 7
    PLAYER = 1
    OPONENTE = 2
    VAZIO = 0
    
    def __init__(self, player = PLAYER):
        self.player = player
        self.board = [[Board.VAZIO] * Board.COLUMNS for row in range(Board.ROWS)]
        self.winner = None
        self.window_winner = []
        self.last_drops = []

    def __repr__(self):
        repr = ''
        for row in self.board:
            srow = list(map(str, row))
            repr += '  '.join(srow) + '\n'
        return repr

    def get(self, row, col):
        return self.board[row][col]
    '''
    def update_winner_positions(self):
        if len(self.window_winner) <= 0:
            return None
        for wn in self.window_winner:
            self.board[wn[0]][wn[1]] = self.winner * 3
    '''

    def change_player(self):
        self.player = 1 if self.player == 2 else 2

    def drop_piece(self, column):
        if self.winner:
            return None
        if column < 0 or column >= Board.COLUMNS:
            return None
        row = 0
        while row < Board.ROWS and self.board[row][column] == Board.VAZIO:
            row += 1
        row-=1
        if row < 0:
            return None
        self.board[row][column] = self.player
        self.last_drops.append((row, column, self.player))
        self.check_winner()
        self.change_player()
        return self

    def check_window(self, window):
        if window.count(self.player) == 4:
            self.winner = self.player
            return True
        return False

    def check_winner(self):
        
        for row in range(Board.ROWS):
            for col in range(Board.COLUMNS-3):
                window = (self.board[row][col],
                         self.board[row][col+1],
                         self.board[row][col+2],
                         self.board[row][col+3])
                if self.check_window(window):
                    self.window_winner = [
                        (row, col), (row, col+1), (row, col+2), (row, col+3)
                    ]
                    return True


        for row in range(Board.ROWS-3):
            for col in range(Board.COLUMNS):
                window = (self.board[row][col],
                         self.board[row+1][col],
                         self.board[row+2][col],
                         self.board[row+3][col])
                if self.check_window(window):
                    self.window_winner = [
                        (row, col), (row+1, col), (row+2, col), (row+3, col)
                    ]
                    return True


        for row in range(Board.ROWS-3):
            for col in range(Board.COLUMNS-3):
                window = (self.board[row][col],
                         self.board[row+1][col+1],
                         self.board[row+2][col+2],
                         self.board[row+3][col+3])
                if self.check_window(window):
                    self.window_winner = [
                        (row, col), (row+1, col+1), (row+2, col+2), (row+3, col+3)
                    ]
                    return True

        for row in range(Board.ROWS-3):
            for col in range(3, Board.COLUMNS):
                window = (self.board[row][col],
                         self.board[row+1][col-1],
                         self.board[row+2][col-2],
                         self.board[row+3][col-3])
                if self.check_window(window):
                    self.window_winner = [
                        (row, col), (row+1, col-1), (row+2, col-2), (row+3, col-3)
                    ]
                    return True
        return False

    def get_valid_positions(self):
        return [col for col in range(Board.COLUMNS) 
                    if self.board[0][col] == Board.VAZIO]


    def back_state(self):
        if not self.last_drops:
            return self
        self.winner = None
        row, column, last_player = self.last_drops.pop()
        self.player = last_player
        self.board[row][column] = Board.VAZIO
        return self

