class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.output = 0

    def add_child(self, place, data):
        if place == 'right':
            self.right = Node(data)
        else:
            self.left = Node(data)

    def print_tree(self):
        if self.left and self.right:
            print(f'{self.left.print_tree()}--{self.data}--{self.right.print_tree()}')
        elif self.left:
            print(f'{self.left.print_tree()}--{self.data}--{self.right}')
        elif self.right:
            print(f'{self.left}--{self.data}--{self.right.print_tree()}')
        else:
            print(f'{self.left}--{self.data}--{self.right}')
        return self.data

    def check_universality(self):
        # traverse
        if self.left:
            self.output += self.left.check_universality()
        if self.right:
            self.output += self.right.check_universality()
        # check for universality
        if self.left is None and self.right is None:
            return self.output + 1
        elif self.left and self.right:
            if self.left.data == self.data == self.right.data:
                return self.output + 1

        return self.output


root = Node(0)
root.add_child('right', 0)
root.add_child('left', 1)
root.right.add_child('left', 1)
root.right.add_child('right', 0)
root.right.left.add_child('left', 1)
root.right.left.add_child('right', 1)
root.print_tree()
print(root.check_universality())
