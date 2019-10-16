import sys
sys.stdin = open('sample_input.txt', 'r')


def BFS(s):
    Q = []

    dx = [0, 1]
    dy = [1, 0]
    Q.append(s)
    visit[s] = True
    while len(Q) != 0:

        for i in range(2):
            x1 = x + dx[i]
            y1 = y + dy[i]


T = int(input())

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

visit = [0] * (N*2 - 1)
x = y = 0
