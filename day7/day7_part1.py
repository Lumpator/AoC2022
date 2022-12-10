file = open("input.txt", "r")
lines = file.readlines()
lines = [line.strip() for line in lines]
current_node = False

def parent_counter(node, value):
    if node.parent:
        node.parent.value += value
        parent_counter(node.parent, value)


class TreeNode:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value
        self.children = []
        self.parent = current_node

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"{self.name}: {self.value}"

    def traverse(self):
        # moves through each node referenced from self downwards
        output = 0
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            if current_node.value < 100000:
                output += current_node.value
            nodes_to_visit += current_node.children
        print(output)

    def calculate_size(self):
        size = self.value
        for child in self.children:
            size += child.value
            if child.children:
                child.calculate_size()
        return size



current_path = []
root = TreeNode("/")
current_node = root
dictionary_sizes = {}


listing = False

for i, line in enumerate(lines):
        if listing:
            if line.split(" ")[0].isdigit():
                current_node.value += int(line.split(" ")[0])
                parent_counter(current_node, int(line.split(" ")[0]))
            else:
                current_node.add_child(TreeNode(line.split(" ")[-1]))
            if i < 1018:
                if "$" in lines[i+1]:
                    listing = False

        else:
            if "$ cd" in line and ".." not in line:
                current_path.append(line.split(" ")[-1])
                for child in current_node.children:
                    if child.name == current_path[-1]:
                        current_node = child
            if ".." in line:
                current_path.pop()
                current_node = current_node.parent
            if "$ ls" in line:
                listing = True

root.traverse()


