# list base

q = []
# enqueue O(1)
q.append(1)
q.append(2)
q.append(3)

# dequeue O(n) 한칸씩 빈칸을 채우기 위해 옮겨줘야함
q.pop(0)

print(q)


# linked list base

from collections import deque

queue = deque()

# enqueue O(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# dequeue O(1)
queue.popleft()
queue.popleft()


print(queue)
