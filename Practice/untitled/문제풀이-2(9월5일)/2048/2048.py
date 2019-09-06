import sys
sys.stdin = open('s_input.txt', 'r')


T = int(input())
for t in range(T):
    N, S = map(str, input().split())
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]

    if S == 'up':
        for i in range(int(N)):
            for j in range(int(N)-1):
                if arr[j][i] == 0:
                    for x in range(1, int(N)-j):
                        if arr[j+x][i] != 0:
                            arr[j][i], arr[j+x][i] = arr[j+x][i], arr[j][i]
                            break
    if S == 'down':
        for i in range(int(N)):
            for j in range(1, int(N)):
                if arr[j][i] == 0:
                    for x in range(1, j):
                        if arr[j-x][i] != 0:
                            arr[j][i], arr[j-x][i] = arr[j-x][i], arr[j][i]
    for ar in arr:
        print(ar)
