import pprint
import sys
sys.stdin = open("input.txt", "r")
for i in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    N, M = len(arr), len(arr[0])

    Max_A = Max_B = Max_C = Max_D = 0
    for i in range(N):
        Sum_A = 0

        for j in range(M):
            Sum_A += arr[i][j]

        if Sum_A > Max_A:
            Max_A = Sum_A

    for i in range(M):
        Sum_B = 0
        for j in range(N):
            Sum_B += arr[j][i]
        if Sum_B > Max_B:
            Max_B = Sum_B

    for diag in range(0, N + M - 1):
        Sum_C = 0
        x = 0 if diag < M else (diag - M + 1)
        y = diag if diag < M else M - 1

        while x < N and y >= 0:
            Sum_C += arr[x][y]
            x += 1
            y -= 1
        if Sum_C > Max_C:
            Max_C = Sum_C

    for diag in range(0, N + M - 1):
        Sum_D = 0
        x = M if diag < M else (diag - M + 1)
        y = diag if diag < M else M - 1
        while x < N and y >= 0:
            Sum_D += arr[x][y]
            x -= 1
            y -= 1
        # print(Sum_D)
        if Sum_D > Max_D:
            Max_D = Sum_D
    print(Max_A, Max_B, Max_C, Max_D)
    print('#{} {}'.format(T, max(Max_A, Max_B, Max_C, Max_D)))
