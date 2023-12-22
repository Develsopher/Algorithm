rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
from collections import deque


def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def bfs(v):
        visited[v] = True
        queue = deque()
        queue.append(v)
        while queue:
            cur_v = queue.popleft()
            for next_v in rooms[cur_v]:
                if visited[next_v] == False:
                    queue.append(next_v)
                    visited[next_v] = True

    bfs(0)

    return all(visited)


print(canVisitAllRooms(rooms))
