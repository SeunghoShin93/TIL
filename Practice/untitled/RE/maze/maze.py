import sys
sys.stdin = open('input.txt', 'r')


def find():
    dRow = [0, 1, 0, -1]
    dCol = [1, 0, -1, 0]
    S = []
    S.append([x, y])
    while len(S) != 0:
        n = S.pop()
        for i in range(4):
            x1 = x + dRow[i]
            y1 = y + dCol[i]
            if 0 <= x1 < N and 0 <= y1 < N:
                if maze[x1][y1] == 3:
                    return 1
                elif maze[x1][y1] == 0:
                    S.append([x1, y1])
                    maze[n[0]][n[1]] = 1


N = 5
maze = [[int(x) for x in input()] for i in range(N)]

for i in range(N):
    if 2 in maze[i]:
        x = i
        y = maze[i].index(2)
