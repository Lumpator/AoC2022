file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = [[0, 0]]

    def move(self, direction):
        if direction == "R":
            self.x += 1
        if direction == "L":
            self.x -= 1
        if direction == "U":
            self.y += 1
        if direction == "D":
            self.y -= 1

    def follow(self, point, direction):
        if "RIGHT" in direction:
            self.x = point.x - 1
            if "UP" in direction:
                self.y = point.y - 1
            elif "DOWN" in direction:
                self.y = point.y + 1
            else:
                self.y = point.y
        elif "LEFT" in direction:
            self.x = point.x + 1
            if "UP" in direction:
                self.y = point.y - 1
            elif "DOWN" in direction:
                self.y = point.y + 1
            else:
                self.y = point.y
        elif "UP" in direction:
            self.y = point.y - 1
            if "LEFT" in direction:
                self.x = point.x + 1
            elif "RIGHT" in direction:
                self.x = point.x - 1
            else:
                self.x = point.x
        elif "DOWN" in direction:
            self.y = point.y + 1
            if "LEFT" in direction:
                self.x = point.x + 1
            elif "RIGHT" in direction:
                self.x = point.x - 1
            else:
                self.x = point.x
        return [self.x, self.y]

    def move_check(self, point):
        output = ""
        if abs(point.x - self.x) > 1:
            output += "X"
        if abs(point.y - self.y) > 1:
            output += "Y"
        return output

    def check_direction(self, point):
        output = ""
        if "X" in self.move_check(point):
            if point.x > self.x:
                output += "RIGHT"
            else:
                output += "LEFT"
        if "Y" in self.move_check(point):
            if point.y > self.y:
                output += "UP"
            else:
                output += "DOWN"
        return output

    def log(self, coordinates):
        if coordinates not in self.visited:
            self.visited.append(coordinates)


knots = [Point(0, 0) for x in range(10)]

for line in lines:
    direction, moves = line.split(" ")[0], int(line.split(" ")[1])
    for _ in range(moves):
        knots[0].move(direction)
        i = 0
        for point in knots[1:]:
            if point.move_check(knots[i]):
                point.log(point.follow(knots[i], point.check_direction(knots[i])))
            i += 1


for point in knots:
    print(len(point.visited))
