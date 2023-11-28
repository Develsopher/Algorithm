class Node:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next

    def remove_back(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def insert_at(self, idx, value):
        new_node = Node(value)
        if idx == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx):
                current = current.next
            new_node.next = current
            current.prev.next = new_node
            new_node.prev = current.prev
            current.prev = new_node

    def remove_at(self, idx, value):
        if idx == 0:
            self.head.prev = None
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(idx):
                current = current.next
            if current.next is None:
                current.prev.next = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def print_all(self):
        current = self.head
        while current:
            print(current.value, end="")
            current = current.next
            if current:
                print("->", end="")
        print()


li = DoubleLinkedList()
li.insert_back(10)
li.insert_back(20)
li.insert_back(30)
li.insert_at(1, 15)
li.print_all()
