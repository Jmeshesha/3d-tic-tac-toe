import time
from isTerminal import isTerminal
import random
import math
from models import Move
# import reader from feed

# takes in the current board and heuristic, and returns best possible move
# A positive value of +1 is given to every n-in-a-row the player has, and a negative value of -1 is given
# for every n-in-a-row the opponent has
HEURISTIC_1 = "counting_n_rows"
# adds a value for every mark that's the player's, minus for every mark that's the opponent's 
HEURISTIC_2 = "counting_marks"
# adds a positive value for every neighbor mark that's empty or the same, but subtracts for opponent's mark
HEURISTIC_3 = "counting_neighbors"
HEURISTIC_4 = "random"

# Types:
# heuristic : String
# board : 3-level array
# board example :  [[["R", G, " "], ["R", "G", " "], ["R", "G", " "]], [["R", "G", " "], ["R", "G", " "], ["R", "G", " "]], [["R", "G", " "], ["R", "G", " "], ["R", "G", " "]]]
# timeInterval : Float
# currPlayer : "R" || "G"
# n : size of board

# TODO
def get_next_move(board, heuristic, timeInterval, currPlayer, opponent, n, onError):
    if heuristic != HEURISTIC_1 and heuristic != HEURISTIC_2 and heuristic != HEURISTIC_3 and heuristic != HEURISTIC_4:
        onError(400, "Invalid Heuristic", "name of heuristic does not match acceptable heuristics")
    # NOTES
    # heuristic will be a string determining which evaluation function we use
    start_move = random.sample(tuple(board.GetPossibleMoves()), 1)[0]# save best_move (value, position)
    start = time.time()
    maxIteration = 1
    bestMove = start_move 
    
    while (time.time() - start) < timeInterval:
        bestEval = - 1
        iterationBestMove = start_move
        leftEarly = False
        state_dict = {}
        for move in board.GetPossibleMoves():
            board.MakeMove(move, currPlayer)
            evaluation = minimax(currPlayer, opponent, board, n, onError, 1, maxIteration, heuristic, start, timeInterval, False, state_dict, move)
            #state_dict[board.getMoveStack()] = (evaluation, True)
            if evaluation > bestEval:
                iterationBestMove = move
                bestEval = evaluation
            board.UndoMove()
            if bestEval >= 1:
                break
            #print(terminal, currPlayer)
            if (time.time() - start) >= timeInterval:
                leftEarly = True
                break
        maxIteration += 1
        
        if not leftEarly:
            bestMove = iterationBestMove
        # start time
    # loop through available moves and check evaluation value with alpha beta minimax iterative deepening
        # call on get_eval_value as looping through
    # do minimax until time runs out
    # returns best move at the end

    return Move(currPlayer, bestMove[0], bestMove[1], bestMove[2])

# NEED TO FINISH
def minimax(maxPlayer, minPlayer, board, n, onError, iteration, maxIteration, heuristic, start_time, timeInterval, isMax, state_dict, move):
    currPlayer = minPlayer
    
    if isMax:
        currPlayer = maxPlayer
    
    terminal = board.getTerminalVal(maxPlayer)
    #terminal = isTerminal(board.GetBoardList(), maxPlayer, n)
    #print(terminal, opponent, move)
    # win 
    if terminal == 1:
        return 1
    # loss 
    if terminal == -1:
        return -1
    # tie
    if terminal == 0:
        return 0
    if iteration >= maxIteration:
        return get_eval_value(board.GetBoardList(), heuristic, maxPlayer, n, onError)
    best_evaluation =  -2 # start at min value (min value should be -1 but going to do -2 just in case) 
    if not isMax:
        best_evaluation = 2
   
    

    for move in board.GetPossibleMoves():
        board.MakeMove(move, currPlayer)
        
        evaluation = minimax(maxPlayer, minPlayer, board, n, onError, iteration+1, maxIteration, heuristic, start_time, timeInterval, not isMax, state_dict, move)
        #print(evaluation)
        board.UndoMove()
        if isMax:
            if evaluation > best_evaluation:
                best_evaluation = evaluation
                if best_evaluation >= 1:
                    return 1
        else:
            if evaluation < best_evaluation:
                best_evaluation = evaluation
            if best_evaluation <= -1:
                    return -1
        if (time.time() - start_time) >= timeInterval:
            break
    
    return best_evaluation

def sigmoid(x):
    return 2 / (1+math.e ** (-x)) - 1


def get_eval_value(new_board, heuristic, currPlayer, n, onError):
    # check string, call on eval function
    if heuristic == HEURISTIC_1:
        return sigmoid(counting_n_rows_eval_function(new_board, currPlayer, n))
    elif heuristic == HEURISTIC_2:
        return sigmoid(counting_marks_eval_function(new_board, currPlayer, n))
    elif heuristic == HEURISTIC_3:
        return sigmoid(counting_neighbors_eval_function(new_board, currPlayer, n))
    elif heuristic == HEURISTIC_4:
        return sigmoid(random_eval_function())
    else:
        onError(400, "Invalid Heuristic", "name of heuristic does not match acceptable heuristics: " + heuristic)
def random_eval_function():
    return random.uniform(-1, 1)
def check_diagonals_on_plane(board, currPlayer, n, plane, score):
    # top left down
    row = 0
    col = 0
    last_value = board[plane][row][col]
    while row < n:
        if board[plane][row][col] == last_value and last_value == currPlayer and row != 0 and col != 0:
            score += 1
        last_value = board[plane][row][col]
        row += 1
        col += 1

    # top right down
    row = 0
    col = n - 1
    last_value = board[plane][row][col]
    while row < n:
        if board[plane][row][col] == last_value and last_value == currPlayer and row != 0 and col != n - 1:
            score += 1
        last_value = board[plane][row][col]
        row += 1
        col -= 1
    return score

# TESTS
# print("Tests on single planes:")
# # # win (1)
# print(check_diagonals_on_plane([[["R", " ", " "], [" ", "R", " "], [" ", " ", "R"]], [[" ", " ", "G"], [" ", "G", " "], ["G", " ", " "]], [[" ", " ", "R"], [" ", "R", " "], ["R", " ", " "]]], "R", 3, 0, 0))
# # loss (-1)
# print(check_diagonals_on_plane([[["R", " ", " "], [" ", " ", " "], [" ", " ", "R"]], [[" ", " ", "G"], [" ", "G", " "], ["G", " ", " "]], [[" ", " ", "R"], [" ", "R", " "], ["R", " ", " "]]], "R", 3, 1, 0))
# # win (1)
# print(check_diagonals_on_plane([[["R", " ", " "], [" ", " ", " "], [" ", " ", "R"]], [[" ", "R", "G"], [" ", "G", " "], ["G", " ", " "]], [["R", " ", " "], [" ", "R", " "], [" ", " ", " "]]], "R", 3, 2, 0))
# print(check_diagonals_on_plane([[[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]], [[" ", "R", "G"], [" ", "G", " "], ["G", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", "R"]]], "R", 3, 2, 0))
    
def check_diagonals_on_sides(board, currPlayer, n, score):
    row = 0
    col = 0
    plane = 0
    # when row = 0 an col = 0 (Front - left top down)
    last_value = board[plane][row][col]
    while plane != n:
        if board[plane][row][col] == last_value and last_value == currPlayer and col != 0 and plane != 0:
            score += 1
        last_value = board[plane][row][col]
        col += 1
        plane += 1

    row = 0
    col = n - 1
    plane = 0
    # when row = 0 and col = n (Front - right top down)
    last_value = board[plane][row][col]
    while plane != n:
        if board[plane][row][col] == last_value and last_value == currPlayer and col != n - 1 and plane != 0:
            score += 1
        last_value = board[plane][row][col]
        col -= 1
        plane += 1
    
    row = 0
    col = 0
    plane = 0
    # col = 0 and row = 0 (Left Side - left top down)
    last_value = board[plane][row][col]
    while plane != n:
        if board[plane][row][col] == last_value and last_value == currPlayer and row != 0 and plane != 0:
            score += 1
        last_value = board[plane][row][col]
        row += 1
        plane += 1

    row = n - 1
    col = 0
    plane = 0
    # col = 0 and row = n (Left Side - right top down)
    last_value = board[plane][row][col]
    while plane != n:
        if board[plane][row][col] == last_value and last_value == currPlayer and row != n - 1 and plane != 0:
            score += 1
        last_value = board[plane][row][col]
        row -= 1
        plane += 1

    row = 0
    col = n - 1
    plane = 0
    # when col = n and row = 0 (Right Side - left top down)
    last_value = board[plane][row][col]
    while plane != n:
        if board[plane][row][col] == last_value and last_value == currPlayer and row != 0 and plane != 0:
            score += 1
        last_value = board[plane][row][col]
        row += 1
        plane += 1
    
    row = n - 1
    col = n - 1
    plane = 0
    # when col = n and row = n (Right Side - right top down)
    last_value = board[plane][row][col]
    while plane != n:
        if board[plane][row][col] == last_value and last_value == currPlayer and row != n - 1 and plane != 0:
            score += 1
        last_value = board[plane][row][col]
        row -= 1
        plane += 1

    row = n - 1
    col = 0
    plane = 0
    # when col = 0 and row = n (Back Side - left top down)
    last_value = board[plane][row][col]
    while plane != n:
        if board[plane][row][col] == last_value and last_value == currPlayer and col != 0 and plane != 0:
            score += 1
        last_value = board[plane][row][col]
        col += 1
        plane += 1

    row = n - 1
    col = n - 1
    plane = 0
    # when col = n and row = n (Back Side - right top down)
    last_value = board[plane][row][col]
    while plane != n:
        if board[plane][row][col] == last_value and last_value == currPlayer and col != n - 1 and plane != 0:
            score += 1
        last_value = board[plane][row][col]
        col -= 1
        plane += 1
    # No wins or losses
    return score

# print(check_diagonals_on_sides([[["R", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], ["R", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]]], "R", 3, 0))
# # loss (-1) Left Side
# print(check_diagonals_on_sides([[[" ", " ", " "], [" ", " ", " "], ["G", " ", " "]], [[" ", " ", " "], ["G", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "G", 3, 0))
# print(check_diagonals_on_sides([[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], ["G", " ", " "], [" ", " ", " "]], [["G", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "G", 3, 0))

# # win (1) Right Side
# print(check_diagonals_on_sides([[[" ", " ", "R"], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", "R"], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]]], "R", 3, 0))
# # loss (-1) Right Side
# print(check_diagonals_on_sides([[[" ", " ", " "], [" ", " ", "G"], [" ", " ", " "]], [[" ", " ", "G"], [" ", " ", "G"], ["G", " ", "G"]], [["G", " ", " "], [" ", " ", "G"], ["G", " ", "G"]]], "G", 3, 0))

# # win (1) Back
# print(check_diagonals_on_sides([[[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", "R", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]]], "R", 3, 0))
# # loss (-1) Back
# print(check_diagonals_on_sides([[[" ", " ", " "], [" ", " ", " "], [" ", " ", "G"]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], ["G", " ", " "]]], "G", 3, 0))

def check_diagonals_on_different_planes(board, currPlayer, n, score):
    # diagonal top left corner 1st plane to bottom right last plane
    col = 0
    row = 0
    plane = 0
    last_value = board[plane][row][col]
    while plane < n:
        if board[plane][row][col] == last_value and last_value == currPlayer and col != 0 and plane != 0:
            score += 1
        last_value = board[plane][row][col]
        col += 1
        row += 1
        plane += 1

    # diagonal top right corner 1st plane to bottom left last plane
    col = n - 1
    row = 0
    plane = 0
    last_value = board[plane][row][col]
    while plane < n:
        if board[plane][row][col] == last_value and last_value == currPlayer and col != n - 1 and row != 0:
            score += 1
        last_value = board[plane][row][col]
        col -= 1
        row += 1
        plane += 1

    # diagonal bottom left corner first plane to right last plane
    col = 0
    row = n - 1
    plane = 0
    last_value = board[plane][row][col]
    while plane < n:
        if board[plane][row][col] == last_value and last_value == currPlayer and plane != 0:
            score += 1
        last_value = board[plane][row][col]
        col += 1
        row -= 1
        plane += 1

    # diagonal bottom right corner irst plane to left last plane
    col = n - 1
    row = n - 1
    plane = 0
    last_value = board[plane][row][col]
    while plane < n:
        if board[plane][row][col] == last_value and last_value == currPlayer and plane != 0:
            score += 1
        last_value = board[plane][row][col]
        col -= 1
        row -= 1
        plane += 1
        
    # front sides to back sides
    col = 0
    row = 0
    plane = 0
    while col != n:
        plane = 0
        row = 0
        last_value = board[plane][row][col]
        while plane < n:
            if board[plane][row][col] == last_value and last_value == currPlayer and row != 0 and plane != 0:
                score += 1
            last_value = board[plane][row][col]
            row += 1
            plane += 1
        col += 1

    # right sides to left sides
    col = n - 1
    row = 1
    plane = 0
    while row != (n - 1):
        plane = 0
        col = n - 1
        last_value = board[plane][row][col]
        while plane < n:
            if board[plane][row][col] == last_value and last_value == currPlayer and plane != 0:
                score += 1
            last_value = board[plane][row][col]
            col -= 1
            plane += 1
        row += 1

    # left sides to right sides
    col = 0
    row = 1
    plane = 0
    while row != (n - 1):
        col = 0
        plane = 0
        last_value = board[plane][row][col]
        while plane < n:
            if board[plane][row][col] == last_value and last_value == currPlayer and plane != 0:
                score += 1
            last_value = board[plane][row][col]
            col += 1
            plane += 1
        row += 1

    # back sides to front sides
    col = 1
    row = n - 1
    plane = 0
    while col != (n - 1):
        row = n - 1
        plane = 0
        last_value = board[plane][row][col]
        while plane < n:
            if board[plane][row][col] == last_value and last_value == currPlayer and plane != 0:
                score += 1
            last_value = board[plane][row][col]
            row -= 1
            plane += 1
        col += 1

    return score

# print(check_diagonals_on_different_planes([[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]]], "R", 3, 0))
# print("Top Right Corner:")
# print(check_diagonals_on_different_planes([[[" ", " ", "R"], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3, 0))
# print("Bottom Left Corner:")
# print(check_diagonals_on_different_planes([[[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]]], "G", 3, 0))
# print("Bottom Right Corner:")
# print(check_diagonals_on_different_planes([[[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [["R", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3, 0))

# print("Front Side:")
# print(check_diagonals_on_different_planes([[[" ", "R", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", "R", " "]]], "R", 3, 0))
# print("Left Side:")
# print(check_diagonals_on_different_planes([[[" ", " ", " "], ["R", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", "R"], [" ", " ", " "]]], "R", 3, 0))
# print("Right Side:")
# print(check_diagonals_on_different_planes([[[" ", " ", " "], [" ", " ", "R"], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], ["R", " ", " "], [" ", " ", " "]]], "R", 3, 0))
# print("Back Side:")
# print(check_diagonals_on_different_planes([[[" ", " ", " "], [" ", " ", " "], [" ", "R", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", "R", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3, 0))

def counting_n_rows_eval_function(new_board, currPlayer, n):
    plane = 0
    row = 0
    col = 0
    score = 0
    while plane < n:
        # each row
        if col == 0:
            temp_col = 0
            last_value = new_board[plane][row][temp_col]
            while temp_col < n:
                if new_board[plane][row][temp_col] == last_value and last_value == currPlayer and temp_col != 0:
                    score += 1
                last_value = new_board[plane][row][temp_col]
                temp_col += 1

        # vertically on one plane
        if row == 0:
            temp_row = 0
            last_value = new_board[plane][temp_row][col]
            while temp_row < n:
                if new_board[plane][temp_row][col] == last_value and last_value == currPlayer and temp_row != 0:
                    score += 1
                last_value = new_board[plane][temp_row][col]
                temp_row += 1

        if plane == 0:
            # vertically on different planes
            temp_plane = 0
            last_value = new_board[temp_plane][row][col]
            while temp_plane < n:
                if new_board[temp_plane][row][col] == last_value and last_value == currPlayer and temp_plane != 0:
                    score += 1
                last_value = new_board[temp_plane][row][col]
                temp_plane += 1
            
        if row == n - 1 and col == n - 1:
            col = 0
            row = 0
            score_to_add = check_diagonals_on_plane(new_board, currPlayer, n, plane, 0)
            score += score_to_add
            plane += 1
            continue

        if col == n - 1:
            col = 0
            row += 1
            continue
        col += 1

    score_to_add = check_diagonals_on_different_planes(new_board, currPlayer, n, 0)
    score += score_to_add

    score_to_add = check_diagonals_on_sides(new_board, currPlayer, n, 0)
    score += score_to_add

    return score

# print(counting_n_rows_eval_function([[["R", "R", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", "R"], [" ", " ", " "], [" ", " ", " "]]], "R", 3))

def counting_marks_eval_function(new_board, currPlayer, n):
    score = 0
    for plane, plane_value in enumerate(new_board):
        for row, row_value in enumerate(plane_value):
            for col, col_value in enumerate(row_value):
                if col_value == currPlayer:
                    score += 1
                if col_value != currPlayer and col_value != " ":
                    score -= 1
    return score

# counting_marks_eval_function([[["R", "G", " "], ["R", "G", " "], ["R", "G", " "]], [["R", "G", " "], ["R", "G", " "], ["R", "G", " "]], [["R", "G", " "], ["R", "G", " "], ["R", "G", " "]]], "R", 3)
# counting_marks_eval_function([[["R", " ", " "], ["R", " ", " "], ["R", " ", " "]], [["R", " ", " "], ["R", " ", " "], ["R", " ", " "]], [["R", " ", " "], ["R", "G", " "], ["R", "G", " "]]], "R", 3)

# +1 neighboring mark or neighboring space
# -1 for neighboring opponent mark
def counting_neighbors_eval_function(new_board, currPlayer, n):
    score = 0
    plane = 0
    row = 0
    col = 0
    while plane < n:
        current_value = new_board[plane][row][col]
        if current_value == currPlayer:
            # left side
            if col != 0:
                if new_board[plane][row][col - 1] == currPlayer or new_board[plane][row][col - 1] == " ":
                    score += 1
                else:
                    score -= 1
            # right side
            if col != (n - 1):
                if new_board[plane][row][col + 1] == currPlayer or new_board[plane][row][col + 1] == " ":
                    score += 1
                else: 
                    score -= 1
            # bottom
            if row != (n - 1):
                if new_board[plane][row + 1][col] == currPlayer or new_board[plane][row + 1][col] == " ":
                    score += 1
                else:
                    score -= 1
            # top
            if row != 0:
                if new_board[plane][row - 1][col] == currPlayer or new_board[plane][row - 1][col] == " ":
                    score += 1
                else:
                    score -= 1
            # left top diagonal
            if row != 0 and col != 0:
                if new_board[plane][row - 1][col - 1] == currPlayer or new_board[plane][row - 1][col - 1] == " ":
                    score += 1
                else:
                    score -= 1
            # right top diagonal
            if row != 0 and col != (n - 1):
                if new_board[plane][row - 1][col + 1] == currPlayer or new_board[plane][row - 1][col + 1] == " ":
                    score += 1
                else:
                    score -= 1
            # left bottom diagonal
            if row != (n - 1) and col != 0:
                if new_board[plane][row + 1][col - 1] == currPlayer or new_board[plane][row + 1][col - 1] == " ":
                    score += 1
                else:
                    score -= 1
            # right bottom diagonal
            if row != (n - 1) and col != (n - 1):
                if new_board[plane][row + 1][col + 1] == currPlayer or new_board[plane][row + 1][col + 1] == " ":
                    score += 1
                else:
                    score -= 1
        if row == n - 1 and col == n - 1:
            col = 0
            row = 0
            plane += 1
            continue

        if col == n - 1:
            col = 0
            row += 1
            continue
        col += 1
    return score


# print(counting_neighbors_eval_function([[["R", " ", "R", "R"], [" ", "R", " ", "R"], [" ", "R", " ", "R"], [" ", "R", " ", "R"]], [[" ", " ", " ", "R"], [" ", " ", " ", "R"], [" ", " ", " ", "R"], [" ", "R", " ", "R"]], [[" ", " ", " ", "R"], [" ", " ", " ", "R"], [" ", " ", " ", "R"], [" ", "R", " ", "R"]], [[" ", " ", " ", "R"], [" ", " ", " ", "R"], [" ", " ", " ", "R"], [" ", "R", " ", "R"]]], "R", 4))
# print(counting_neighbors_eval_function([[["R", " ", "R"], [" ", "R", " "], [" ", "R", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))
# print(counting_neighbors_eval_function([[["R", "G", "R"], ["G", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))
# print(counting_neighbors_eval_function([[["R", "G", "R"], [" ", "G", " "], ["G", " ", " "]], [[" ", " ", "G"], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))
# print(counting_neighbors_eval_function([[["R", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))
# print(counting_neighbors_eval_function([[["G", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))
# print(counting_neighbors_eval_function([[[" ", " ", " "], [" ", "R", " "], [" ", "R", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", "G", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))