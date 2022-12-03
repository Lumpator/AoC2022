file = open("day3_backpack.txt", "r")
lines = file.readlines()

badges = []

i = 0
while i < len(lines) - 2:
    for char in (lines[i].strip()):
        if char in (lines[i + 1]) and char in (lines[i + 2]):
            # check for the first character that appears in 3 lines together
            badges.append(char)
            break
    i += 3


def calculate_priority(char):
    if char.lower() == char:
        return ord(char) - 96
    return ord(char) - 64 + 26


priority_sum = 0
for badge in badges:
    priority_sum += calculate_priority(badge)

print(priority_sum)
