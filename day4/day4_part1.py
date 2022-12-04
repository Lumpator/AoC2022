file = open("day4_input.txt", "r")
lines = file.readlines()

pairs = [line.strip().split(",") for line in lines]


def converter(pair):
    return [int(x) for x in pair.split("-")]


def check_if_range_in_range(list_of_pairs):
    pair1 = converter(list_of_pairs[0])
    pair2 = converter(list_of_pairs[1])
    if pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
        return True
    if pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
        return True
    return False


output = 0
for pair in pairs:
    if check_if_range_in_range(pair):
        output += 1

print(output)
