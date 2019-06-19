class Node:
    def __init__(self, element):
        self.element = element
        self.next_index = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_whole_list(self):
        temp = self.head
        while temp:
            print(temp.element)
            temp = temp.next_index


llobject = LinkedList()
llobject.head = Node(1)
second = Node(2)
third = Node(3)

llobject.head.next_index = second
second.next_index = third

llobject.print_whole_list()
