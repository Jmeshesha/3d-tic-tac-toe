from aivsai import ai_v_ai
from tournament import run_tournaments
import numpy as np
from itertools import permutations
from matplotlib import pyplot as plt
import matplotlib
evaluation_functions = ["counting_n_rows", "counting_marks", "counting_neighbors"]

def run_randomplayer_evaluation(boardSize, timeInterval, games):
    print("running randomplayer for", boardSize, "x", boardSize, "x", boardSize, "board with timeinterval:", timeInterval)
    winRatio = {}
    for evaluation_function in evaluation_functions:
        winRatio[evaluation_function + "_first"] = 0
        winRatio[evaluation_function + "_second"] = 0
        for i in range(games):
            winner1 = ai_v_ai(boardSize, boardSize, boardSize, boardSize, evaluation_function, "random", timeInterval, None)
            if winner1 == evaluation_function:
                winRatio[evaluation_function + "_first"] += 1 
            winner2 = ai_v_ai(boardSize, boardSize, boardSize, boardSize, "random", evaluation_function, timeInterval, None)
            if winner2 == evaluation_function:
                winRatio[evaluation_function + "_second"] += 1 

        winRatio[evaluation_function + "_first"] /= games
        winRatio[evaluation_function + "_second"] /= games
    return winRatio 

 
def run_direct_evaluation(boardSize, timeCutoff, games):
    print("running direct for", boardSize, "x", boardSize, "x", boardSize, "board with timeinterval:", timeCutoff)
    winRatio = {}
    for evals in permutations(evaluation_functions, 2):
        heuristic1, heuristic2 = evals
        winRatio[heuristic1 + "vs" + heuristic2] = 0
        for i in range(games):
            winner = ai_v_ai(boardSize, boardSize, boardSize, boardSize, heuristic1, heuristic2, timeCutoff, None)
            if winner == heuristic1:
                winRatio[heuristic1 + "vs" + heuristic2] += 1
        winRatio[heuristic1 + "vs" + heuristic2] /= games
    return winRatio


def run_tournament_evaluation(boardSize, timeCutoff, tournaments):
    print("running tornament for", boardSize, "x", boardSize, "x", boardSize, "board with timeinterval:", timeCutoff)
    return run_tournaments(boardSize, boardSize, boardSize, boardSize, evaluation_functions, timeCutoff, tournaments)

timeIntervals = [0.0025, 0.005, 0.0075, 0.01, 0.0125, 0.015 , 0.0175, 0.02]
#timeIntervals = [0.0001, 0.0002, 0.0003]
experiments = [run_randomplayer_evaluation, run_direct_evaluation, run_tournament_evaluation]

def run_experiments():
    
    for boardSize in range(3, 6):
        random_player_data = {}
        direct_data = {}
        tournament_data = {}
        for timeCutoff in timeIntervals:
            data = run_randomplayer_evaluation(boardSize, timeCutoff, 50)
            for point in data.keys():
                random_player_data[point] = random_player_data.get(point, [])  + [data[point]]
            data = run_direct_evaluation(boardSize, timeCutoff, 50)
            for point in data.keys():
                direct_data[point] = direct_data.get(point, [])  + [data[point]]
            data = run_tournament_evaluation(boardSize, timeCutoff, 50)
            for point in data.keys():
                tournament_data[point] = tournament_data.get(point, [])  + [data[point]]
        title = "Random Player Evaluation " + str(boardSize) + "X" + str(boardSize) + "X" + str(boardSize)
        plot_data(random_player_data, timeIntervals, title)
        title = "Direct Evaluation " + str(boardSize) + "X" + str(boardSize) + "X" + str(boardSize)
        plot_data(direct_data, timeIntervals, title)
        title = "Tournament Evaluation " + str(boardSize) + "X" + str(boardSize) + "X" + str(boardSize)
        plot_data(tournament_data, timeIntervals, title)
           

def plot_data(wins, timeCutoffs, title):
    plt.clf()
    matplotlib.rc('font', size=6)
    for key in wins.keys():
        plt.plot(timeCutoffs, wins[key], label = key)
    plt.xlabel("Time intervals")
    plt.ylabel("Win ratio")
    plt.title(title)
    plt.legend(loc="upper left")
    file_title = title.replace(" ", "_")
    figure = plt.gcf() # get current figure
    figure.set_size_inches(8, 6)
    plt.savefig("PythonServer/plots/" +file_title + ".png", dpi = 100)
run_experiments()


