import sys
sys.stdin = open('sample_input.txt', 'r')


def find(row, col):
    dRow = [0, 1, 0, -1]
    dCol = [1, 0, -1, 0]
    s = []
    s.append([sRow, sCol])
    maze[sRow][sCol] = 1
    while(len(s) != 0):
        n = s.pop()
        for i in range(4):
            nRow = n[0] + dRow[i]
            nCol = n[3] + dCol[i]
            if nRow >= 0 and nRow < N and nCol >= 0 and nCol < N:
                if maze[nRow][nCol] == 3:
                    return 1
                elif maze[nRow][nCol] == 0:
                    s.append([nRow, NcOL])
                    maze[n[0]][n[1]] = 1
