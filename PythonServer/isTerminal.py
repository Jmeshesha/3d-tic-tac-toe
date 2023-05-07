def check_diagonals_on_plane(board, currPlayer, n, plane):
    # top left down
    row = 0
    col = 0
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while row < n:
            if board[plane][row][col] == value_to_check:
                row += 1
                col += 1
                continue
            else:
                break
        if row == n:
            if value_to_check == currPlayer:
                return 1
            else:
                return -1

    # top right down
    row = 0
    col = n - 1
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while row < n:
            if board[plane][row][col] == value_to_check:
                row += 1
                col -= 1
                continue
            else:
                break
        if row == n:
            if value_to_check == currPlayer:
                return 1
            else:
                return -1
    return None
# TESTS
# print("Tests on single planes:")
# # win (1)
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
        while plane != n:
            if board[plane][row][col] == value_to_check:
                col += 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1

    row = 0
    col = n - 1
    plane = 0
    # when row = 0 and col = n (Front - right top down)
    value_to_check = board[0][row][col]
    if value_to_check != " ":
        while plane != n:
            if board[plane][row][col] == value_to_check:
                col -= 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1
    
    row = 0
    col = 0
    plane = 0
    # col = 0 and row = 0 (Left Side - left top down)
    value_to_check = board[0][0][0]
    if value_to_check != " ":
        while plane != n:
            if board[plane][row][col] == value_to_check:
                row += 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1

    row = n - 1
    col = 0
    plane = 0
    # col = 0 and row = n (Left Side - right top down)
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while plane != n:
            if board[plane][row][col] == value_to_check:
                row -= 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1

    row = 0
    col = n - 1
    plane = 0
    # when col = n and row = 0 (Right Side - left top down)
    value_to_check = board[0][row][col]
    if value_to_check != " ":
        while plane != n:
            if board[plane][row][col] == value_to_check:
                row += 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1
    
    row = n - 1
    col = n - 1
    plane = 0
    # when col = n and row = n (Right Side - right top down)
    value_to_check = board[0][row][col]
    if value_to_check != " ":
        while plane != n:
            if board[plane][row][col] == value_to_check:
                row -= 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1

    row = n - 1
    col = 0
    plane = 0
    # when col = 0 and row = n (Back Side - left top down)
    value_to_check = board[0][row][col]
    if value_to_check != " ":
        while plane != n:
            if board[plane][row][col] == value_to_check:
                col += 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1

    row = n - 1
    col = n - 1
    plane = 0
    # when col = n and row = n (Back Side - right top down)
    value_to_check = board[0][row][col]
    if value_to_check != " ":
        while plane != n:
            if board[plane][row][col] == value_to_check:
                col -= 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1
    # No wins or losses
    return None

# win (1) Left Side
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
        while plane < n:
            if board[plane][row][col] == value_to_check:
                col += 1
                row += 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1

    # diagonal top right corner 1st plane to bottom left last plane
    col = n - 1
    row = 0
    plane = 0
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while plane < n:
            if board[plane][row][col] == value_to_check:
                col -= 1
                row += 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1

    # diagonal bottom left corner first plane to right last plane
    col = 0
    row = n - 1
    plane = 0
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while plane < n:
            if board[plane][row][col] == value_to_check:
                col += 1
                row -= 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1

    # diagonal bottom right corner irst plane to left last plane
    col = n - 1
    row = n - 1
    plane = 0
    value_to_check = board[plane][row][col]
    if value_to_check != " ":
        while plane < n:
            if board[plane][row][col] == value_to_check:
                col -= 1
                row -= 1
                plane += 1
                continue
            else:
                break
        if plane == n and value_to_check == currPlayer:
            return 1
        if plane == n and value_to_check != currPlayer:
            return -1

    # front sides to back sides
    col = 1
    row = 0
    plane = 0
    while col != (n - 1):
        value_to_check = board[plane][row][col]
        if value_to_check != " ":
            while plane < n:
                if board[plane][row][col] == value_to_check:
                    row += 1
                    plane += 1
                    continue
                else:
                    break
            if plane == n and value_to_check == currPlayer:
                return 1
            if plane == n and value_to_check != currPlayer:
                return -1
        col += 1

    # right sides to left sides
    col = n - 1
    row = 1
    plane = 0
    while row != (n - 1):
        value_to_check = board[plane][row][col]
        if value_to_check != " ":
            while plane < n:
                if board[plane][row][col] == value_to_check:
                    col -= 1
                    plane += 1
                    continue
                else:
                    break
            if plane == n and value_to_check == currPlayer:
                return 1
            if plane == n and value_to_check != currPlayer:
                return -1
        row += 1

    # left sides to right sides
    col = 0
    row = 1
    plane = 0
    while row != (n - 1):
        value_to_check = board[plane][row][col]
        if value_to_check != " ":
            while plane < n:
                if board[plane][row][col] == value_to_check:
                    col += 1
                    plane += 1
                    continue
                else:
                    break
            if plane == n and value_to_check == currPlayer:
                return 1
            if plane == n and value_to_check != currPlayer:
                return -1
        row += 1

    # back sides to front sides
    col = 1
    row = n - 1
    plane = 0
    while col != (n - 1):
        value_to_check = board[plane][row][col]
        if value_to_check != " ":
            while plane < n:
                if board[plane][row][col] == value_to_check:
                    row -= 1
                    plane += 1
                    continue
                else:
                    break
            if plane == n and value_to_check == currPlayer:
                return 1
            if plane == n and value_to_check != currPlayer:
                return -1
        col += 1

    return None

def isTerminal(board, currPlayer, n):
    plane = 0
    row = 0
    col = 0
    empty_spaces = 0
    while plane < n:

        current_value = board[plane][row][col]
        
        # check spaces
        if current_value == " ":
            empty_spaces += 1

        current_value = board[plane][row][col]
        # check for win or loss in each row
        if col == 0:
            temp_col = 0
            while temp_col < n:
                if board[plane][row][temp_col] == board[plane][row][col]:
                    temp_col += 1
                    continue
                else:
                    break
            if temp_col == n and board[plane][row][col] == currPlayer:
                return 1
            if temp_col == n and board[plane][row][col] != currPlayer and board[plane][row][col] != " ":
                return -1

        current_value = board[plane][row][col]
        # check for win or loss vertically on one plane
        if row == 0:
            temp_row = 0
            while temp_row < n:
                if board[plane][temp_row][col] == board[plane][row][col]:
                    temp_row += 1
                    continue
                else:
                    break
            if temp_row == n and current_value == currPlayer:
                return 1
            if temp_row == n and current_value != currPlayer and board[plane][row][col] != " ":
                return -1

        current_value = board[plane][row][col]
        if plane == 0:
            # check for win or loss vertically on different planes
            temp_plane = 0
            while temp_plane < n:
                if board[temp_plane][row][col] == current_value:
                    temp_plane += 1
                    continue
                else:
                    break
            if temp_plane == n and current_value == currPlayer:
                return 1
            if temp_plane == n and current_value != currPlayer:
                return -1

        if row == n - 1 and col == n - 1:
            col = 0
            row = 0
            check = check_diagonals_on_plane(board, currPlayer, n, plane)
            plane += 1
            if check == 1:
                return 1
            if check == -1:
                return -1
            continue

        if col == n - 1:
            col = 0
            row += 1
            continue

        col += 1

    check2 = check_diagonals_on_different_planes(board, currPlayer, n)
    if check2 == 1:
        return 1
    if check2 == -1:
        return -1

    check3 = check_diagonals_on_sides(board, currPlayer, n)
    if check3 == 1:
        return 1
    if check3 == -1:
        return -1

    if empty_spaces == 0:
        return 0
    return None

# # TESTS
# print(isTerminal([[[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']], [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', 'g', ' ']], [[' ', ' ', 'g', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']], [['r', 'r', 'r', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]], 'g', 4))
# print(isTerminal([[[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']], [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']], [[' ', ' ', 'g', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']], [['r', 'r', 'g', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]], 'g', 4))
# print(isTerminal([[['r', ' ', ' '], ['r', ' ', ' '], ['r', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]], 'g', 3))
# print(isTerminal([[['r', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [['r', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], [['r', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]], 'g', 3))
# # win (1) Front
# # print("Front Sides:")
# print(isTerminal([[["R", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]]], "R", 3))
# # loss (-1) Front
# print(isTerminal([[[" ", " ", "G"], [" ", " ", " "], [" ", " ", " "]], [[" ", "G", " "], [" ", " ", " "], [" ", " ", " "]], [["G", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))

# # win (1)
# print("Top Left Corner:")
# print(isTerminal([[["R", " ", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]]], "R", 3))
# print("Top Right Corner:")
# print(isTerminal([[[" ", " ", "R"], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]]], "R", 3))
# print("Bottom Left Corner:")
# print(isTerminal([[[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], ["R", " ", " "]]], "R", 3))
# print("Bottom Right Corner:")
# print(isTerminal([[[" ", " ", " "], [" ", " ", " "], [" ", " ", "R"]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [["R", " ", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))

# print("Front Side:")
# print(isTerminal([[[" ", "R", " "], [" ", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", " "], [" ", "R", " "]]], "R", 3))
# print("Left Side:")
# print(isTerminal([[[" ", " ", " "], ["R", " ", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], [" ", " ", "R"], [" ", " ", " "]]], "R", 3))
# print("Right Side:")
# print(isTerminal([[[" ", " ", " "], [" ", " ", "R"], [" ", " ", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", " ", " "], ["R", " ", " "], [" ", " ", " "]]], "R", 3))
# print("Back Side:")
# print(isTerminal([[[" ", " ", " "], [" ", " ", " "], [" ", "R", " "]], [[" ", " ", " "], [" ", "R", " "], [" ", " ", " "]], [[" ", "R", " "], [" ", " ", " "], [" ", " ", " "]]], "R", 3))