from pprint import pprint

file = open("day3_backpack.txt", "r")
lines = file.readlines()

items = []
for line in lines:
    backpack_items = ""
    for char in (line.strip())[0:(int(len(line.strip()) / 2))]:  # iterate through chars in first half of string
        if char in (line.strip())[(int(len(line.strip()) / 2)):]:  # check, if char is in second half of string
            if char not in backpack_items: #check for duplicities in one backpack
                backpack_items += char
    items.append(backpack_items)


def calculate_priority(char):
    if char.lower() == char:
        return ord(char) - 96
    return ord(char) - 64 + 26


priority_sum = 0
for item in items:
    priority_sum += calculate_priority(item)

print(priority_sum)




