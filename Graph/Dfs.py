# 인접 리스트로 그래프 표현
graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["A", "B"],
    "E": ["A"],
}

visited = []


# def dfs(cur_v):
#     visited.append(cur_v)
#     for v in graph[cur_v]:
#         if v not in visited:
#             dfs(v)


# dfs("A")


def dfs(graph, cur_v, visited=[]):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            visited = dfs(graph, v)
    return visited
