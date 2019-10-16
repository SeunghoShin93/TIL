from collections import deque
import sys
sys.stdin = open('graph_input.txt', 'r')


def BFS(s, G):
    visit = [False] * (V+1)
    D = [0] * E

    Q = deque()
    Q.append(s)
    visit[s] = True
    print(s, end=' ')
    while len(Q) != 0:
        v = Q.pop()
        for w in G[v]:
            if not visit[w]:
                D[w] = D[v] + 1
                visit[w] = True
                Q.append(w)
                print(w, end=' ')
    print()
    return D


V, E = map(int, input().split())

G = [[] for _ in range(V+1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

D = BFS(1, G)
print(D[1:])
