from pprint import pprint
from typing import List

file = open("da2_rps.txt", "r")
lines = file.readlines()

all_rounds = []
for line in lines:  # create list of lists with each round from input .txt
    round = []
    for char in line.strip().replace(" ", "").replace("X", "A").replace("Y", "B").replace("Z", "C"):
        round.append(char)
    all_rounds.append(round)

point_table = {"A": 1, "B": 2, "C": 3, "DRAW": 3, "WIN": 6, "LOSS": 0}
moves = ["A", "B", "C"]


def calculate_winner(round: List):
    if round[0] == round[1]:
        return "DRAW"
    if moves[moves.index(round[1]) - 1] == round[0]:
        """   
            When you place moves like: ROCK,PAPER,SCISSORS,
            you will win when your oppopent's move is in 1 position left from your move.
            I just take index of move 1 left (or last if my move is first) and check if I won or not.
            
        """
        return "WIN"
    return "LOSS"


def calculate_points(result, move):
    return point_table[result] + point_table[move]


total_score = 0
for round in all_rounds:
    total_score += calculate_points(calculate_winner(round), round[1])

print(total_score)
