# keys and rooms
# rooms [[1], [2], [3], []] -> True
# rooms [[1,3], [3,0,1] ,[2], [0]] -> False
# rooms [[1, 3], [2, 4], [0], [4], [],[3, 4]]


# O(V + E)

# DFS
# 방갯수 n
# dfs할때 이동길이 count
# if 이동길이 n 되는순간 return True
rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]


def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    # v에 연결되어있는 모든 vertex에 방문할거임
    def dfs(v):
        visited[v] = True
        for next_v in rooms[v]:
            if visited[next_v] == False:
                # if next_v not in visited:  # O(n) #index가 없어서
                dfs(next_v)

    dfs(0)
    # return visited
    if len(visited) == len(rooms):
        return True
    else:
        return False


print(canVisitAllRooms(rooms))
# BFS


from collections import deque


def canVisitAllRooms2(rooms):
    visited = [False] * len(rooms)

    def bfs(v):
        queue = deque()
        queue.append(v)
        visited[v] = True
        while queue:
            cur_v = queue.popleft()
            for next_v in rooms[cur_v]:
                if visited[next_v] == False:
                    queue.append(next_v)
                    visited.append(next_v)

    bfs(0)

    # return visited
    if len(visited) == len(rooms):
        return True
    else:
        return False
