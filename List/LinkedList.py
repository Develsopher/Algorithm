class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = None

    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, idx, value):
        new_node = Node(value)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, idx):
        if idx == 0:
            self.haed = self.head.next
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            current.next = current.next.next

    def get(self, idx):
        if idx < 0 or idx >= self.size:
            raise Exception("out of range")
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def print(self):
        current = self.head
        while current:
            print(current.value, end="")
            current = current.next
            if current:
                print("->", end="")
        print()


li = LinkedList()
li.insert_back(1)
li.insert_back(2)
li.insert_back(3)
li.insert_back(4)
li.insert_back(5)
li.print()
