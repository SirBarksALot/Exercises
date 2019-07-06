class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def print(self):
        if self.left is None:
            if self.right is None:
                print(f'{None}--{self.data}--{None}')
            else:
                print(f'{None}--{self.data}--{self.right.print()}')

        else:
            if self.right is None:
                print(f'{self.left.print()}--{self.data}--{None}')
            else:
                print(f'{self.left.print()}--{self.data}--{self.right.print()}')
        return self.data


root = Node(15)
root.insert(22)
root.insert(2)
root.insert(7)
root.insert(1)
root.insert(16)
root.print()
