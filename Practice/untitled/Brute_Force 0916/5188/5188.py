import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    tmp = [[0]*N] * N

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                tmp[i][j] = arr[i][j]

            elif i == 0:
                tmp[i][j] = arr[i][j] + tmp[i][j-1]
            elif j == 0:
                tmp[i][j] = arr[i][j] + tmp[i-1][j]
            else:
                tmp[i][j] = min(arr[i][j] + tmp[i-1][j],
                                arr[i][j] + tmp[i][j-1])

    print('#{} {}'.format(t, tmp[N-1][N-1]))
