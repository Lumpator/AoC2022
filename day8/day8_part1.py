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


not_visible = 0
for index, line in enumerate(lines):
    if index == 0 or index == 98:
        pass
    else:
        for idx, char in enumerate(line):
            if idx == 0 or idx == 98:
                pass
            else:
                if int(char) <= max([int(x) for x in line[:idx]]) and int(char) <= max(
                        [int(x) for x in line[idx + 1:]]) and int(char) <= int(
                        max(create_list_top(index, idx, lines))) and int(char) <= int(max(create_list_down(index, idx, lines))):
                    not_visible += 1





print(99 * 99 - not_visible)
