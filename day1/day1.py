file = open("day1.txt", "r")
lines = file.readlines()

elves = {}
i = 1

for line in lines:
    if line.strip():
        if i not in elves:
            elves[i] = 0
        elves[i] += int(line)
    else:
        i += 1

print(max(elves.values()))

#part2

sorted_elves = sorted(elves.values(), reverse=True)[0:3]

print(sum(sorted_elves))


