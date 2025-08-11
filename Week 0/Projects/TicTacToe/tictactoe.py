"""
Tic Tac Toe Player
"""

import math
import copy

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

    counter = 0

    for i in range(3):
        for j in range(3):
            if(board[i][j] != EMPTY):
                counter = counter + 1

    if(counter % 2):
        return O
    
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    all_possible_actions = set()

    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                all_possible_actions.add((i,j))

    return all_possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultant_board = copy.deepcopy(board)
    resultant_board[action[0]][action[1]] = player(board)
    return resultant_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    """Horizontal Check"""
    for i in range(3):
        score = 0
        for j in range(3):
            if(board[i][j] == X):
                score = score + 1
            elif(board[i][j] == O):
                score = score - 1
        if(score == 3):
            return X
        elif(score == -3):
            return O

    """Vertical Check"""
    for i in range(3):
        score = 0
        for j in range(3):
            if(board[j][i] == X):
                score = score + 1
            elif(board[j][i] == O):
                score = score - 1
        if(score == 3):
            return X
        elif(score == -3):
            return O

    """Left to Right Diagonal Check"""
    score = 0
    for i in range(3): 
        if(board[i][i] == X):
            score = score + 1
        elif(board[i][i] == O):
            score = score - 1
    if(score == 3):
        return X
    elif(score == -3):
        return O

    """Right to Left Diagonal Check"""
    i=0
    j=2
    score = 0
    while(i<3):
        if(board[i][j] == X):
            score = score + 1
        elif(board[i][j] == O):
            score = score - 1
        i = i + 1
        j = j - 1
    if(score == 3):
        return X
    elif(score == -3):
        return O

    return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) != None):
        return True

    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if(w == X):
        return 1
    
    elif (w == O):
        return -1
    
    return 0


def min_value(board):
    if(terminal(board)):
        return utility(board),None

    v = math.inf
    opt_action = None
    
    for action in actions(board):
        m = copy.deepcopy(v)
        v = min(v,max_value(result(board,action))[0])
        if(m != v):
            opt_action = action

    return (v,opt_action)
    
    
def max_value(board):
    if(terminal(board)):
        return utility(board),None
    
    v = -math.inf
    opt_action = None
    for action in actions(board):
        m = copy.deepcopy(v)
        v = max(v,min_value(result(board,action))[0])
        if(m != v):
            opt_action = action

    return (v,opt_action)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    
    if(player(board) == X):
        return max_value(board)[1]
        
    else:
        return min_value(board)[1]
            
        
