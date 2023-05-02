# takes in the current board and heuristic, and returns best possible move
HEURISTIC_1 = ""
HEURISTIC_2 = ""
HEURISTIC_3 = ""

def get_next_move(self, board, heuristic, time):
    if heuristic != HEURISTIC_1 or heuristic != HEURISTIC_2 or heuristic != HEURISTIC_3:
        return "Please enter a correct heuristic function"
    # heuristic will be a string determining which evaluation function we use
    # board will be a matrix
    best_move = (0,position) # save best_move (value, position)
    # loop through available moves and check evaluation value
    
    # NOTES
    # do minimax until time runs out
def get_eval_value(self, position, heuristic):
    # check string, call on eval function
    if heuristic == HEURISTIC_1:
        self.eval_function_1(position)
    else if heuristic == HEURISTIC_2:
        self.eval_function_2(position)
    else:
        self.eval_function_3(position)  

def eval_function_1(self, position):

def eval_function_2(self, position):

def eval_function_3(self, position):