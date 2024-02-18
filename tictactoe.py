"""
Tic Tac Toe Player
"""

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """ 
    all_empty = all(col == EMPTY for row in board for col in row)
    count_x = sum(row.count('X') for row in board)
    count_o = sum(row.count('O') for row in board)
    
    if all_empty:
        return X
    elif count_x > count_o:
        return O
    else: return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] >2 or action[1] > 2 or action[0] < 0 or action[1] < 0:
        raise ValueError("Invalid action: {}".format(action))
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid action: {}".format(action)) 
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(0, 3):
        if (board[row][0] != EMPTY) and (board[row][0] == board[row][1] == board[row][2]):
            return board[row][0]
    for col in range(0, 3):
        if (board[0][col] != EMPTY) and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    if (board[0][0] != EMPTY) and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if (board[0][2] != EMPTY) and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else: return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    ai_player = player(board)
    max_eval = -float('inf')
    min_eval = float('inf')
    best_move = None

    for action in actions(board):
        result_board = result(board, action)
        result_score = mini_value(result_board) if ai_player == X else max_value(result_board)
        
        if ai_player == X and result_score == 1:
            return action
        elif ai_player == O and result_score == -1:
            return action

        if (ai_player == X and result_score > max_eval):
            max_eval = result_score
            best_move = action
        elif ai_player == O and result_score < min_eval:
            min_eval = result_score
            best_move = action

    return best_move

def max_value(board):
    if terminal(board):
        return utility(board)

    max_eval = -float('inf')

    for action in actions(board):
        result_board = result(board, action)
        result_score = mini_value(result_board)
        max_eval = max(max_eval, result_score)

    return max_eval

def mini_value(board):
    if terminal(board):
        return utility(board)

    min_eval = float('inf')

    for action in actions(board):
        result_board = result(board, action)
        result_score = max_value(result_board)
        min_eval = min(min_eval, result_score)

    return min_eval
