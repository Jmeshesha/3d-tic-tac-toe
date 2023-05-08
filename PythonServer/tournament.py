from aivsai import ai_v_ai
from itertools import permutations
import random

def run_match(planes, rows, cols, n,  heuristic1_idx, heuristic2_idx, tournament_status, timePerTurn):
    heuristic_1 = tournament_status[heuristic1_idx]
    heuristic_2 = tournament_status[heuristic2_idx]
    winner_to_loser_idx = {
        heuristic_1: heuristic2_idx, 
        heuristic_2: heuristic1_idx, 
        "Tie": random.choice([heuristic1_idx, heuristic2_idx])}
    
    winner = ai_v_ai(planes, rows, cols, n, heuristic_1, heuristic_2, timePerTurn, None)
    loser_idx = winner_to_loser_idx[winner]
    return tournament_status[:loser_idx] + tournament_status[loser_idx + 1:]

def run_tournament(planes, rows, cols, n, heuristic_order, timePerTurn):
    tournament_status = heuristic_order
    while len(tournament_status) > 1:
        if len(tournament_status) % 2 == 1:
            tournament_status = run_match(planes, rows, cols, n, 0, 1, tournament_status, timePerTurn)
        newStatus = tournament_status
        for i in range(0, len(tournament_status), 2):
            newStatus = run_match(planes, rows, cols, n, i, i+1, tournament_status, timePerTurn)
        tournament_status = newStatus
    return tournament_status[0]


def run_tournaments(planes, rows, cols, n, heuristics, timePerTurn, tournaments_amount):
    wins = {}
    for heuristic in heuristics:
        wins[heuristic] = 0
    counter = 0
    while counter < tournaments_amount: 
        heuristic_order = random.choice(list(permutations(heuristics, len(heuristics))))
        wins[run_tournament(planes, rows, cols, n, heuristic_order, timePerTurn)] += 1
        counter += 1
    print(wins)
    return wins
        

run_tournaments(5, 5, 5, 5, ["counting_n_rows", "counting_marks", "counting_neighbors"], 0.01, 100)