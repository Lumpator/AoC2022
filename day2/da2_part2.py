from pprint import pprint
from typing import List

file = open("da2_rps.txt", "r")
lines = file.readlines()

all_rounds = []
for line in lines:  # create list of lists with each round from input .txt
    round = []
    for char in line.strip().replace(" ", ""):
        round.append(char)
    all_rounds.append(round)

point_table = {"A": 1, "B": 2, "C": 3, "Y": 3, "Z": 6, "X": 0}
moves = ["A", "B", "C"]


def calculate_points(round):
    if round[1] == "Y":
        return 3 + point_table[round[0]]
    if round[1] == "X":
        return point_table[moves[
            moves.index(round[0]) - 1]]  # LOSS means my move is in moves index on 1 position left to opponents move
    else:
        return 6 + point_table[moves[moves.index(round[0]) - 2]]


total_score = 0
for round in all_rounds:
    total_score += calculate_points(round)

print(total_score)
