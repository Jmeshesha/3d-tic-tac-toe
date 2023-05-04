import time
# import reader from feed

# takes in the current board and heuristic, and returns best possible move
# A positive value of +1 is given to every n-in-a-row the player has, and a negative value of -1 is given
# for every n-in-a-row the opponent has
HEURISTIC_1 = "counting-n-rows"
# adds a value for every mark that's the player's, minus for every mark that's the opponent's 
HEURISTIC_2 = "counting-marks"
# adds a positive value for every neighbor mark that's empty or the same, but subtracts for opponent's mark
HEURISTIC_3 = "counting-neighbors"

# Types:
# heuristic : String
# board : 3-level array
# board example :  [[["R", G, " "], ["R", "G", " "], ["R", "G", " "]], [["R", "G", " "], ["R", "G", " "], ["R", "G", " "]], [["R", "G", " "], ["R", "G", " "], ["R", "G", " "]]]
# timeInterval : Float
# currPlayer : "R" || "G"
# n : size of board

# TODO
def get_next_move(board, heuristic, timeInterval, currPlayer, n):
    if heuristic != HEURISTIC_1 and heuristic != HEURISTIC_2 and heuristic != HEURISTIC_3:
        onError(400, "Invalid Heuristic", "name of heuristic does not match acceptable heuristics")
    # NOTES
    # heuristic will be a string determining which evaluation function we use
    best_move = (0,0) # save best_move (value, position)
    start = time.perf_counter()
    print(start)
    check = time.perf_counter()
    print(time = check - start)
    # start time
    # loop through available moves and check evaluation value with alpha beta minimax iterative deepening
        # call on get_eval_value as looping through
    # do minimax until time runs out
    # returns best move at the end
    return best_move[1]

# NEED TO FINISH
def minimax(isMaxTurn, currPlayer, board, n):
    # win 
    if isTerminal(board, currPlayer, n) == 1:
        return 1
    # loss 
    elif isTerminal(board, currPlayer, n) == -1:
        return -1
    # tie
    elif isTerminal(board, currPlayer, n) == 0:
        return 0

# NEED TO TEST 
def isTerminal(board, currPlayer, n):
    plane = 0
    row = 0
    col = 0
    empty_spaces = 0
    while plane <= n:
        current_value = board[plane][row][col]
        # check spaces
        if current_value == " ":
            empty_spaces += 1
            col += 1
            continue
        if row > n and col > n:
            col = 0
            row = 0
            plane += 1
        if col > n:
            col = 0
            row += 1
        # check for win or loss in each row
        if col == 0:
            temp_col = 1
            while temp_col <= n:
                if board[plane][row][temp_col] == current_value:
                    temp_col += 1
                else:
                    break
            if temp_col > n and current_value == currPlayer:
                return 1
            if temp_col > n and current_value != currPlayer:
                return -1

            
        # check for win or loss vertically on one plane
        if row == 0:
            temp_row = 1
            while temp_row <= n:
                if board[plane][temp_row][col] == current_value:
                    temp_row += 1
                else:
                    break
            if temp_row > n and current_value == currPlayer:
                return 1
            if temp_row > n and current_value != currPlayer:
                return -1

        if plane == 0:
            # check for win or loss vertically on different planes
            temp_plane = 1
            while temp_plane <= n:
                if board[temp_plane][row][col] == current_value:
                    temp_plane += 1
                else:
                    break
            if temp_plane > n and current_value == currPlayer:
                return 1
            if temp_plane > n and current_value != currPlayer:
                return -1
        row += 1

    if empty_spaces == 0:
        return 0
    return None


def check_diagonals_on_plane(board, currPlayer, n, plane):
    # top left down
    row = 0
    col = 0
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while row < (n - 1):
            row += 1
            col += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if row == n - 1:
            if value_to_check == currPlayer:
                return 1
            else:
                return -1

    # top right down
    row = 0
    col = n - 1
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while row < (n - 1):
            row += 1
            col -= 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if row == n - 1:
            if value_to_check == currPlayer:
                return 1
            else:
                return -1
# TESTS
# print("Tests on single planes:")
# win (1)
# print(check_diagonals_on_plane([[["R", " ", " "], [" ", "R", " "], [" ", " ", "R"]], [[" ", " ", "G"], [" ", "G", " "], ["G", " ", " "]], [[" ", " ", "R"], [" ", "R", " "], ["R", " ", " "]]], "R", 3, 0))
# # loss (-1)
# print(check_diagonals_on_plane([[["R", " ", " "], [" ", "R", " "], [" ", " ", "R"]], [[" ", " ", "G"], [" ", "G", " "], ["G", " ", " "]], [[" ", " ", "R"], [" ", "R", " "], ["R", " ", " "]]], "R", 3, 1))
# # win (1)
# print(check_diagonals_on_plane([[["R", " ", " "], [" ", "R", " "], [" ", " ", "R"]], [[" ", " ", "G"], [" ", "G", " "], ["G", " ", " "]], [[" ", " ", "R"], [" ", "R", " "], ["R", " ", " "]]], "R", 3, 2))


def check_diagonals_on_sides(board, currPlayer, n):
    row = 0
    col = 0
    plane = 0
    # when row = 0 an col = 0 (Front - left top down)
    value_to_check = board[0][0][0]
    if value_to_check != " ":
        while plane < (n - 1):
            col += 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1

    row = 0
    col = n - 1
    plane = 0
    # when row = 0 and col = n (Front - right top down)
    value_to_check = board[0][row][col]
    if value_to_check != " ":
        while plane < (n - 1):
            col -= 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1
    
    row = 0
    col = 0
    plane = 0
    # col = 0 and row = 0 (Left Side - left top down)
    value_to_check = board[0][0][0]
    if value_to_check != " ":
        while plane < (n - 1):
            row += 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1

    row = n - 1
    col = 0
    plane = 0
    # col = 0 and row = n (Left Side - right top down)
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while plane < (n - 1):
            row -= 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1

    row = 0
    col = n - 1
    plane = 0
    # when col = n and row = 0 (Right Side - left top down)
    value_to_check = board[0][row][col]
    if value_to_check != " ":
        while plane < (n - 1):
            row += 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1
    
    row = n - 1
    col = n - 1
    plane = 0
    # when col = n and row = n (Right Side - right top down)
    value_to_check = board[0][row][col]
    if value_to_check != " ":
        while plane < (n - 1):
            row -= 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1

    row = n - 1
    col = 0
    plane = 0
    # when col = 0 and row = n (Back Side - left top down)
    value_to_check = board[0][row][col]
    if value_to_check != " ":
        while plane < (n - 1):
            col += 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1

    row = n - 1
    col = n - 1
    plane = 0
    # when col = n and row = n (Back Side - right top down)
    value_to_check = board[0][row][col]
    if value_to_check != " ":
        while plane < (n - 1):
            col -= 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1
    # No wins or losses
    return None

# TESTS
# win (1) Front
# print("Front Sides:")
# print(check_diagonals_on_sides([[["R", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", "R", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", "R"], [" ", " ", " "], [" ", " ", " "]]], "R", 3))
# # loss (-1) Front
# print(check_diagonals_on_sides([[[" ", " ", "G"], [" ", " ", " "], [" ", " ", " "]], [[" ", "G", " "], [" ", " ", " "], [" ", " ", " "]], [["G", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))

# # win (1) Left Side
# print("Left Sides:")
# print(check_diagonals_on_sides([[["R", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], ["R", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]]], "R", 3))
# # loss (-1) Left Side
# print(check_diagonals_on_sides([[[" ", " ", " "], [" ", " ", " "], ["G", " ", " "]], [[" ", " ", " "], ["G", " ", " "], [" ", " ", " "]], [["G", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))

# print("Right Sides:")
# # win (1) Right Side
# print(check_diagonals_on_sides([[[" ", " ", "R"], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", "R"], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]]], "R", 3))
# # loss (-1) Right Side
# print(check_diagonals_on_sides([[[" ", " ", " "], [" ", " ", " "], [" ", " ", "G"]], [[" ", " ", " "], [" ", " ", "G"], [" ", " ", " "]], [[" ", " ", "G"], [" ", " ", " "], [" ", " ", " "]]], "R", 3))

# print("Back Sides:")
# # win (1) Back
# print(check_diagonals_on_sides([[[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", "R", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]]], "R", 3))
# # loss (-1) Back
# print(check_diagonals_on_sides([[[" ", " ", " "], [" ", " ", " "], [" ", " ", "G"]], [[" ", " ", " "], [" ", " ", " "], [" ", "G", " "]], [[" ", " ", " "], [" ", " ", " "], ["G", " ", " "]]], "R", 3))


def check_diagonals_on_different_planes(board, currPlayer, n):
    # diagonal top left corner 1st plane to bottom right last plane
    col = 0
    row = 0
    plane = 0
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while plane < (n - 1):
            col += 1
            row += 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1

    # diagonal top right corner 1st plane to bottom left last plane
    col = n - 1
    row = 0
    plane = 0
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while plane < (n - 1):
            col -= 1
            row += 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1

    # diagonal bottom left corner first plane to right last plane
    col = 0
    row = n - 1
    plane = 0
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while plane < (n - 1):
            col += 1
            row -= 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1

    # diagonal bottom right corner irst plane to left last plane
    col = n - 1
    row = n - 1
    plane = 0
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while plane < (n - 1):
            col -= 1
            row -= 1
            plane += 1
            if board[plane][row][col] == value_to_check:
                continue
            else:
                break
        if plane == (n - 1) and value_to_check == currPlayer:
            return 1
        if plane == (n - 1) and value_to_check != currPlayer:
            return -1

    # front sides to back sides
    col = 1
    row = 0
    plane = 0
    while col != (n - 1):
        value_to_check = board[plane][row][col]
        if value_to_check != " ":
            while plane < (n - 1):
                row += 1
                plane += 1
                if board[plane][row][col] == value_to_check:
                    continue
                else:
                    break
            if plane == (n - 1) and value_to_check == currPlayer:
                return 1
            if plane == (n - 1) and value_to_check != currPlayer:
                return -1
        col += 1

    # right sides to left sides
    col = n - 1
    row = 1
    plane = 0
    while row != (n - 1):
        value_to_check = board[plane][row][col]
        if value_to_check != " ":
            while plane < (n - 1):
                col -= 1
                plane += 1
                if board[plane][row][col] == value_to_check:
                    continue
                else:
                    break
            if plane == (n - 1) and value_to_check == currPlayer:
                return 1
            if plane == (n - 1) and value_to_check != currPlayer:
                return -1
        row += 1

    # left sides to right sides
    col = 0
    row = 1
    plane = 0
    while row != (n - 1):
        value_to_check = board[plane][row][col]
        if value_to_check != " ":
            while plane < (n - 1):
                col += 1
                plane += 1
                if board[plane][row][col] == value_to_check:
                    continue
                else:
                    break
            if plane == (n - 1) and value_to_check == currPlayer:
                return 1
            if plane == (n - 1) and value_to_check != currPlayer:
                return -1
        row += 1

    # back sides to front sides
    col = 1
    row = n - 1
    plane = 0
    while col != (n - 1):
        value_to_check = board[plane][row][col]
        if value_to_check != " ":
            while plane < (n - 1):
                row -= 1
                plane += 1
                if board[plane][row][col] == value_to_check:
                    continue
                else:
                    break
            if plane == (n - 1) and value_to_check == currPlayer:
                return 1
            if plane == (n - 1) and value_to_check != currPlayer:
                return -1
        col += 1

    return None

# win (1) 
# print("Top Left Corner:")
# print(check_diagonals_on_different_planes([[["R", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]]], "R", 3))
# print("Top Right Corner:")
# print(check_diagonals_on_different_planes([[[" ", " ", "R"], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]]], "R", 3))
# print("Bottom Left Corner:")
# print(check_diagonals_on_different_planes([[[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]]], "R", 3))
# print("Bottom Right Corner:")
# print(check_diagonals_on_different_planes([[[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [["R", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))

# print("Front Side:")
# print(check_diagonals_on_different_planes([[[" ", "R", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", "R", " "]]], "R", 3))
# print("Left Side:")
# print(check_diagonals_on_different_planes([[[" ", " ", " "], ["R", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", "R"], [" ", " ", " "]]], "R", 3))
# print("Right Side:")
# print(check_diagonals_on_different_planes([[[" ", " ", " "], [" ", " ", "R"], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], ["R", " ", " "], [" ", " ", " "]]], "R", 3))
# print("Back Side:")
# print(check_diagonals_on_different_planes([[[" ", " ", " "], [" ", " ", " "], [" ", "R", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", "R", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))

def get_eval_value(new_board, heuristic, currPlayer, n):
    # check string, call on eval function
    if heuristic == HEURISTIC_1:
        return counting_n_rows_eval_function(new_board, currPlayer, n)
    if heuristic == HEURISTIC_2:
        counting_marks_eval_function(new_board, currPlayer, n)
    if heuristic == HEURISTIC_3:
        counting_neighbors_eval_function(new_board, currPlayer, n)
    else:
        onError(400, "Invalid Heuristic", "name of heuristic does not match acceptable heuristics")


# TODO check diagonals on different planes
def counting_n_rows_eval_function(new_board, currPlayer, n):
    # if there's an error
    col = 0
    row = 0
    plane = 0
    score = 0 # 1000 = win , -1000 = loss
    empty_spaces = 0
    while True:
        current_value = new_board[plane][row][col]
        # check if empty space 
        if current_value == " ":
            empty_spaces += 1

        # checking n-in-a-row for player
        if current_value == currPlayer:
            # check vertically on different planes
            if plane == 0:
                # check if win vertically
                if new_board[1][row][col] == currPlayer and new_board[2][row][col] == currPlayer:
                    score = 1000
                    print(score)
                    break
                if new_board[1][row][col] == currPlayer:
                    score += 1
                if new_board[2][row][col] == currPlayer:
                    score += 1
                
                # check diagonals on different planes

            # check vertically on same plane
            if row == 0:
                # check if win vertically
                if new_board[plane][1][col] == currPlayer and new_board[plane][2][col] == currPlayer and new_board[plane][0][col] == currPlayer:
                    score = 1000
                    print(score)
                    break
                if new_board[plane][1][col] == currPlayer:
                    score += 1
                if new_board[plane][2][col] == currPlayer:
                    score += 1

        # checking n-in-a-row for opponent
        if current_value != currPlayer and current_value != " ":
            # check vertically on different planes
            if plane == 0:
                # check if loss vertically
                if new_board[1][row][col] == current_value and new_board[2][row][col] == current_value:
                    score = -1000
                    print(score)
                    break
                if new_board[1][row][col] == current_value:
                    score -= 1
                if new_board[2][row][col] == current_value:
                    score -= 1

            # check vertically on same plane
            if row == 0:
                # check for loss
                if new_board[1][row][col] == current_value and new_board[2][row][col] == current_value and new_board[0][row][col] == current_value:
                    score = -1000
                    print(score)
                    break
                if new_board[plane][1][col] != currPlayer and new_board[plane][1][col] != " ":
                    score -= 1
                if new_board[plane][2][col] != currPlayer and new_board[plane][2][col] != " ":
                    score -= 1
        
        # checking row for player
        if col != 0:
            if current_value == currPlayer and new_board[plane][row][0] == currPlayer:
                score += 1
            if current_value != currPlayer and current_value != " " and new_board[plane][row][0] == current_value:
                score -= 1
        col += 1
        print(current_value)
        print(score)

        # reached the end of the board so we break out of while loop
        if plane == 2 and row == 2 and col == 3:
            # check for diagonals on different planes
            # if new_board:
            break

        # reached the end of the plane
        if row == 2 and col == 3:
            # check diagonals on plane
            if new_board[plane][0][0] == currPlayer:
                if new_board[plane][1][1] == currPlayer:
                    score += 1
                    if new_board[plane][2][2] == currPlayer:
                        score = 1000
                        break
            if new_board[plane][0][0] != currPlayer and new_board[plane][0][0] != " ":
                if new_board[plane][1][1] != currPlayer and new_board[plane][1][1] != " ":
                    score -= 1
                    if new_board[plane][2][2] != currPlayer and new_board[plane][2][2] != " ":
                        score = -1000
                        break
            plane += 1
            row = 0
            col = 0
            continue
        # reached end of row so start at new row on plane
        if col == 3:
            # check for win in the row
            if new_board[plane][row][1] == currPlayer and new_board[plane][row][0] == currPlayer and new_board[plane][row][2]: #win
                score = 1000
                break
            row += 1
            col = 0
            continue
    return score

# counting_rows_eval_function([[["R", "R", "G"], [" ", "R", " "], ["R", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R")

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

def counting_neighbors_eval_function(new_board, currPlayer, n):
    score = 0
    for plane, plane_value in enumerate(new_board):
        for row, row_value in enumerate(plane_value):
            for col, col_value in enumerate(row_value):
                if col_value == currPlayer:
                    score += 1
                if col_value != currPlayer and col_value != " ":
                    score -= 1
    return score



# get_next_move([[["R", "G", " "], ["R", "G", " "], ["R", "G", " "]], [["R", "G", " "], ["R", "G", " "], ["R", "G", " "]], [["R", "G", " "], ["R", "G", " "], ["R", "G", " "]]], "counting-marks", 2, "R", 3)