import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N-K+1):
            if j == 0:
                if arr[i][j] == 1:
                    for x in range(1, K):
                        if arr[i][j+x] == 0:
                            break
                    else:
                        if arr[i][j+K] == 0:
                            cnt += 1
                            continue
            if j == N-K:
                if arr[i][j] == 1:
                    for x in range(1, K):
                        if arr[i][j+x] == 0:
                            break
                    else:
                        if arr[i][j-1] == 0:
                            cnt += 1
                            continue
            else:
                if arr[i][j] == 1:
                    for x in range(1, K):
                        if arr[i][j+x] == 0:
                            break
                    else:
                        if arr[i][j-1] == 0 and arr[i][j+K] == 0:
                            cnt += 1

    for i in range(N-K+1):
        for j in range(N):
            if i == 0:
                if arr[i][j] == 1:
                    for x in range(1, K):
                        if arr[i+x][j] == 0:
                            break
                    else:
                        if arr[i+K][j] == 0:
                            cnt += 1
                            continue
            elif i == N-K:
                if arr[i][j] == 1:
                    for x in range(1, K):
                        if arr[i+x][j] == 0:
                            break
                    else:
                        if arr[i-1][j] == 0:
                            cnt += 1
                            continue
            else:
                if arr[i][j] == 1:
                    for x in range(1, K):
                        if arr[i+x][j] == 0:
                            break
                    else:
                        if arr[i-1][j] == 0 and arr[i+K][j] == 0:
                            cnt += 1

    print('#{} {}'.format(t, cnt))
