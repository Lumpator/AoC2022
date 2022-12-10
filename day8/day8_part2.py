file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]


def create_list_top(index, idx, lines):
    list = []
    for i, line in enumerate(lines):
        if i >= index:
            pass
        else:
            list.append(int(line[idx]))
    return list


def create_list_down(index, idx, lines):
    list = []
    for i, line in enumerate(lines):
        if i <= index:
            pass
        else:
            list.append(int(line[idx]))
    return list


def calculate_sceneric_score_left(char, idx, line):
    score = 0
    i = -1
    list = [int(x) for x in line[:idx]]
    while True:
        if abs(i) > len(list):
            break
        if int(char) > int(list[i]):
            score += 1
            i -= 1
        else:
            score += 1
            break
    return score

def calculate_sceneric_score_top(char, list):
    score = 0
    i = -1
    while True:
        if abs(i) > len(list):
            break
        if int(char) > int(list[i]):
            score += 1
            i -= 1
        else:
            score += 1
            break
    return score

def calculate_sceneric_score_right(char, idx, line):
    score = 0
    i = 0
    list = [int(x) for x in line[idx+1:]]
    while True:
        if i == len(list):
            break
        if int(char) > int(list[i]):
            score += 1
            i += 1
        else:
            score += 1
            break
    return score

def calculate_sceneric_score_bot(char, list):
    score = 0
    i = 0
    while True:
        if i == len(list):
            break
        if int(char) > int(list[i]):
            score += 1
            i += 1
        else:
            score += 1
            break
    return score


sceneric_scores = []

for index, line in enumerate(lines):
    if index == 0 or index == 98:
        pass
    else:
        for idx, char in enumerate(line):
            if idx == 0 or idx == 98:
                pass
            else:
                sceneric_scores.append(calculate_sceneric_score_left(char, idx, line)
                                       * calculate_sceneric_score_right(char, idx, line)
                                       * calculate_sceneric_score_top(char, create_list_top(index, idx, lines))
                                       * calculate_sceneric_score_bot(char, create_list_down(index, idx, lines))
                                       )


print(max(sceneric_scores))