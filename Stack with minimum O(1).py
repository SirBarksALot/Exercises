class Stack:
    def __init__(self):
        self.stack_list = []

    def insert(self, number):
        if len(self.stack_list) >= 1:
            var = self.stack_list[-1]
            if number >= var:
                self.stack_list.append(var)
                self.stack_list[-2] = number
            else:

                self.stack_list.append(number)
        else:
            self.stack_list.append(number)

    def pop(self):
        self.stack_list.pop()

    def print_stack(self):
        print(self.stack_list)


stack = Stack()
stack.insert(3)
stack.insert(2)
stack.insert(5)
stack.insert(7)
stack.print_stack()
