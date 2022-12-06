import re

stack1 = list("NCRTMZP")
stack2 = list("DNTSBZ")
stack3 = list("MHQRFCTG")
stack4 = list("GRZ")
stack5 = list("ZNRH")
stack6 = list("FHSWPZLD")
stack7 = list("WDZRCGM")
stack8 = list("SJFLHWZQ")
stack9 = list("SQPWN")
stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

file = open("input.txt", "r")
lines = file.readlines()[10:]

commands = []
for line in lines:
    commands.append(re.findall(r'\d+', line.strip()))

for command in commands:
    i = 0
    while i < int(command[0]):
        stacks[(int(command[2]) - 1)].append(stacks[(int(command[1]) - 1)].pop())
        i += 1

output = ""
for stack in stacks:
    output += stack[-1]

print(output)