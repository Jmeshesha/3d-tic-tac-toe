# takes in the current board and heuristic, and returns best possible move
HEURISTIC_1 = ""
# HEURISTIC_2 = ""
# HEURISTIC_3 = ""

# Types:
# heuristic : String
# board : 3-level array
# board example :  [[["R", G, " "], ["R", "G", " "], ["R", "G", " "]], [["R", "G", " "], ["R", "G", " "], ["R", "G", " "]], [["R", "G", " "], ["R", "G", " "], ["R", "G", " "]]]
# timeInterval : Float
# currPlayer : "R" || "G"

# TODO
def get_next_move(board, heuristic, timeInterval, currPlayer):
    if heuristic != HEURISTIC_1 or heuristic != HEURISTIC_2 or heuristic != HEURISTIC_3:
        return "Please enter a correct heuristic function"
    # NOTES
    # heuristic will be a string determining which evaluation function we use
    best_move = (0,position) # save best_move (value, position)
    # start time
    # loop through available moves and check evaluation value with alpha beta minimax iterative deepening
        # call on get_eval_value as looping through
    # do minimax until time runs out
    # returns best move at the end
    return best_move[1]

def get_eval_value(position, heuristic):
    # check string, call on eval function
    if heuristic == HEURISTIC_1:
        return eval_function_1(position)
    else:
        print("Invalid heuristic")
    # else if heuristic == HEURISTIC_2:
    #     eval_function_2(position)
    # else if:
    #     eval_function_3(position)

# TODO
def eval_function_1(position):
    # if there's an error
    return None

# def eval_function_2(self, position):

# def eval_function_3(self, position):