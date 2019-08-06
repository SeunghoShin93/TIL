import sys
sys.stdin = open("input.txt", "r")
for i in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    N, M = len(arr), len(arr[0])

    Max = 0
    for i in range(N):
        Sum = 0
        for j in range(M):
            Sum += arr[i][j]
        Max = max(Max, Sum)

    for i in range(M):
        Sum = 0
        for j in range(N):
            Sum += arr[j][i]
        Max = max(Max, Sum)

    for i in range(M):
        Sum = 0
        for j in range(N):
            Sum += arr[i][i]
        Max = max(Max, Sum)

    for i in range(M):
        Sum = 0
        for j in range(N):
            Sum += arr[i][99-i]
        Max = max(Max, Sum)

    # for i in range(100):
    #     Sum = 0
    #     x = 0 if diag < M else (diag - M + 1)
    #     y = diag if diag < M else M - 1

    #     while x < N and y >= 0:
    #         Sum_C += arr[x][y]
    #         x += 1
    #         y -= 1
    #     if Sum_C > Max:
    #         Max = Sum_C

    # for diag in range(0, N + M - 1):
    #     Sum_D = 0
    #     x = 0 if diag < M else (diag - M + 1)
    #     y = diag if diag < M else 0
    #     while x < N and y >= 0:
    #         Sum_D += arr[x][y]
    #         x += 1
    #         y -= 1
        # print(Sum_D)

    print('#{} {}'.format(T, Max))
