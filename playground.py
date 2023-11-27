# class Node:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next


# class LinkedList(object):
#     def __init__(self):
#         self.head = None

#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def get(self, idx):
#         current = self.head
#         for _ in range(idx):
#             current = current.next
#         return current.value

#     def insert(self, idx, value):
#         new_node = Node(value)
#         if idx == 0:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             current = self.head
#             for _ in range(idx - 1):
#                 current = current.next
#             new_node.next = current.next
#             current.next = new_node

#     def remove(self, idx):
#         if idx == 0:
#             self.head = self.head.next
#         else:
#             current = self.head
#             for _ in range(idx - 1):
#                 current = current.next
#             current.next = current.next.next


# li = LinkedList()
# li.append(1)
# li.append(2)
# li.append(3)
# print(li.get(1))

class BrowserHistory(object):
  def __init__(self, homepage):

  def visit(self, url):

  def back(self, steps):

  def forward(self, steps):
    