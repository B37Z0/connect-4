# Connect 4

def create_board():
    '''
    (None) -> List(List(str))
    Create 6x7 board comprising 2D nested list. Slots are empty " " strings.
    '''
    board = []
    for i in range(6):
        row = []
        for j in range(7):
            row.append(" ")
        board.append(row)
    return board


def print_board(board):
    '''
    Print current game board in a readable format with colors.
    'X' tokens are printed in red, 'O' tokens in yellow, and empty cells are uncolored.
    '''
    # Colors
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    for row in board:
        row_string = "|"
        for cell in row:
            if cell == 'X':
                row_string += RED+" X"+RESET+" |"
            if cell == 'O':
                row_string += YELLOW+" O"+RESET+" |"
            if cell == " ":
                row_string += "   |"
        print(row_string)
    # Line for bottom of the board
    print("*****************************")


def drop_token(board, column, token):
    '''
    Drop a token. Returns True if valid, False otherwise.
    '''

    if column >= len(board[0]) or column < 0 or isinstance(column, int) != True:
        print("Invalid column number!")
        return False

    # Start checking for validity from bottom row
    i = len(board)-1
    while i >= 0:
        # Place in first empty row
        if board[i][column] == " ":
            board[i][column] = token
            return True
        i -= 1

    # Otherwise, the column is full
    print("Column is full!")
    return False


def check_horizontal(board, token):
    '''
    Check for a horizontal win. True if 4 consecutive tokens, False otherwise.
    '''
    for row in board: # iterate over all rows
        
        # initialize the count value
        count = 0
        
        for cell in row: # iterate over all columns in the row
            # if column contains the token, increment the counter
            if cell == token:
                count += 1
            # the column doesn't contain the token, so reset the counter
            if cell != token: 
                count = 0
            # if the count reaches 4, we have a winner...
            if count == 4:
                True

    # no winning pattern found, return false
    return False

def check_vertical(board, token):
    '''
    Check for a vertical win. True if 4 consecutive tokens, False otherwise.
    '''

    N_rows = len(board)
    N_cols = len(board[0])
    
    # Iterate through each row
    x = 0
    while x < N_cols:
        # Iterate through all columns for the row
        y = 0
        count = 0
        while y < N_rows:
            if board[y][x] == token:
                count += 1
            if board[y][x] != token:
                count = 0
            if count == 4:
                return True
            y += 1
        x += 1
    # If no vertical win, return False
    return False

def check_diagonals(board, token):
    '''
    Check for a diagonal win. True if 4 consecutive tokens, False otherwise.
    '''

    N_rows = len(board)
    N_cols = len(board[0])

    # Diagonals from top-left to bottom-right.
    for row in range(N_rows - 3):  # Loop until 3 rows before the bottom.
        for col in range(N_cols - 3):  # Loop until 3 columns before the right edge.
            if (board[row][col] == token and
                board[row + 1][col + 1] == token and
                board[row + 2][col + 2] == token and
                board[row + 3][col + 3] == token):
                return True

    # Diagonals from bottom-left to top-right.
    for row in range(3, N_rows):  # Loop starting from the 4th row (index 3) to the bottom.
        for col in range(N_cols - 3):  # Loop until 3 columns before the right edge.
            if (board[row][col] == token and
                board[row - 1][col + 1] == token and
                board[row - 2][col + 2] == token and
                board[row - 3][col + 3] == token):
                return True
    return False

def check_winner(board, token):
    '''
    Check if the specified token has a winning sequence of 4.
    '''
    if check_horizontal(board, token) or check_vertical(board, token) or check_diagonals(board, token):
        return True
    else:
        return False

def check_board_full(board):
    '''
    Check if the board is full.
    '''
    
    for row in board:
        for col in row:
            if col == ' ':
                return False
    return True

def play_game():
    '''
    Game loop.
    '''
    # Initialize board. Starting player = "X"
    board = create_board()
    print_board(board)
    players = ["X", "O"]
    count = 0
    current_player = players[count]

    game_over = False
    while not game_over:
        print("Player " + current_player + "'s turn:")
        column = int(input(f"Choose a column [1-7]: ")) - 1
        
        if not drop_token(board, column, current_player):
            print("Invalid column. Please select a different column.")

        else:
            print_board(board)

            if check_winner(board, current_player):
                print("Player " + current_player + " won!")
                game_over = True
            elif check_board_full(board):
                print("Board full. Draw!")
                game_over = True

            count = (count + 1) % 2
            current_player = players[count]

play_game()
