from models import Board
from isTerminal import isTerminal
from nextMove import get_next_move
from concurrent.futures import ThreadPoolExecutor
import time
def ai_v_ai(planes, rows, cols, n, heuristic1, heuristic2, timePerTurn, onError):
    request = {
        "board": [ord(" ")] * planes * rows * cols,
        "planes": planes,
        "rows": rows,
        "cols": cols,
        "inARow": n,
        "emptyPiece": ord(" ")
    }
    player1 = ord("R")
    player2 = ord("G")    
    board = Board(request)
    turn = 0
    terminalVal = None
    while(terminalVal == None):
        if turn % 2 == 0:
            takeTurn(player1, player2, board, heuristic1, timePerTurn, n, onError)
            
        else:
            takeTurn(player2, player1, board, heuristic2, timePerTurn, n, onError)
        
        turn += 1
        terminalVal = board.getTerminalVal(player1)
        

        
    if terminalVal == 1:
        return heuristic1
    elif terminalVal == -1: 
        return heuristic2
    else:
        return "tie"

def takeTurn(player, opponent, board, heuristic, timePerTurn, n, onError):
    board_move = get_next_move(board, heuristic, timePerTurn, player, opponent, n, onError)
    move = (board_move.plane, board_move.row, board_move.col)
    board.MakeMove(move, player)
def errFunc(errorCode, name, description):
    print(errorCode, name, description)
def playGame(plane, row, col,n, heuristic1, heuristic2, timePerTurn):
    return ai_v_ai(plane, row, col,n, heuristic1, heuristic2, timePerTurn, errFunc)

def playGames_Threads(plane, row, col,n, heuristic1, heuristic2, timePerTurn, games, threads):
    
    futures = []
    executor = ThreadPoolExecutor(threads)
    winner_dict = {heuristic1: 0, heuristic2: 0, "tie": 0}
    for i in range(games):
        future = executor.submit(playGame, plane, row, col, n, heuristic1, heuristic2, timePerTurn)
        futures.append(future)
    for i in range(games):
        winner_dict[futures[i].result()] += 1

    return winner_dict

def playGames(plane, row, col,n, heuristic1, heuristic2, timePerTurn, games):
    winner_dict = {heuristic1: 0, heuristic2: 0, "tie": 0}
    for i in range(games):
        winner = ai_v_ai(plane, row, col,n, heuristic1, heuristic2, timePerTurn, errFunc)
        winner_dict[winner] += 1
    return winner_dict
#print(playGames(5, 5, 5, 5,"counting_n_rows", "counting_neighbors", 0.01, 100))
