file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

cycle = 1
important_cycles = [20, 60, 100, 140, 180, 220]
instructions = []


class Instruction:
    def __init__(self, cycle, value):
        self.ending_cycle = cycle + 2
        self.value = value


for line in lines:
    if line == "noop":
        cycle += 1
    else:
        instructions.append(Instruction(cycle, int(line.split(" ")[1])))
        cycle += 2

output = 0
for x in important_cycles:
    output += x * ((sum([instruction.value for instruction in instructions if instruction.ending_cycle <= x])) + 1)

cursor = 1
cycle = 1
result = []
row = ""
for i in range(instructions[-1].ending_cycle):
    cursor = ((sum([instruction.value for instruction in instructions if instruction.ending_cycle <= cycle])) + 1)
    if len(row) + 1 not in range(cursor, cursor + 3):
        row += "."
    else:
        row += "#"
    cycle += 1
    if len(row) == 40:
        result.append(row)
        row = ""
result.append(row)

for row in result:
    print(row)
