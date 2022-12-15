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
        if direction == "RIGHT":
            self.x = point.x - 1
            self.y = point.y
        elif direction == "LEFT":
            self.x = point.x + 1
            self.y = point.y
        elif direction == "UP":
            self.x = point.x
            self.y = point.y - 1
        elif direction == "DOWN":
            self.x = point.x
            self.y = point.y + 1
        return [self.x, self.y]

    def move_check(self, point):
        # if abs(point.x - self.x) == 2 and abs(point.y - self.y) == 2:
        #     return "DIAGONAL"
        if abs(point.x - self.x) > 1:
            return "X"
        if abs(point.y - self.y) > 1:
            return "Y"
        else:
            return False

    def check_direction(self, point):
        if self.move_check(point) == "X":
            if point.x > self.x:
                return "RIGHT"
            else:
                return "LEFT"
        if self.move_check(point) == "Y":
            if point.y > self.y:
                return "UP"
            else:
                return "DOWN"

    def log(self, coordinates):
        if coordinates not in self.visited:
            self.visited.append(coordinates)


head = Point(0, 0)
tail = Point(0, 0)

for line in lines:
    direction, moves = line.split(" ")[0], int(line.split(" ")[1])
    for _ in range(moves):
        head.move(direction)
        if tail.move_check(head):
            tail.log(tail.follow(head, tail.check_direction(head)))
            head.visited.append([head.x, head.y])


print(len(tail.visited))



