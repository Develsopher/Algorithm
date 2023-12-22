rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]


def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def dfs(v):
        visited[v] = True
        for next_v in rooms[v]:
            if visited[next_v] == False:
                dfs(next_v)

    dfs(0)

    return all(visited)


print(canVisitAllRooms(rooms))
