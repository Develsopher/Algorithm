# Linked List
class Node(object):
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class BrowserHistory(object):
    def __init__(self, homepage):
        new_node = Node(homepage)
        self.head = self.current = new_node

    def visit(self, url):
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = self.current.next

    def back(self, steps):
        for _ in range(steps):
            if self.current.prev:
                self.current = self.current.prev
            else:
                break
        return self.current.value

    def forward(self, steps):
        for _ in range(steps):
            if self.current.next:
                self.current = self.current.next
            else:
                break
        return self.current.value


# input
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

test = BrowserHistory("leetcode.com")
test.visit("google.com")
test.back(1)
