class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print(self):
        print('{}--{}--{}'.format(self.left, self.data, self.right))


root = Node(15)
root.print()
