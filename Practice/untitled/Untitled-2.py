arr = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [4, 5, 7], [3, 6]]


def BFS(G, v):
    n = 7
    visited = [0] * n
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            visit[t]
        for i in G[t]:
            if not visited[i]:
                queue.append(i)


BFS(arr, 1)
