import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    if t > 1:
        print()
    print('#{}'.format(t))
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # (0, N)   (N, N)    (N, 0)
    x = 0
    y = N-1

    for x in range(N):
        if x > 0:
            print()
        for i in range(N-1, -1, -1):
            print(arr[i][x], end='')

        print(' ', end='')
        for j in range(N-1, -1, -1):
            print(arr[y][j], end='')

        print(' ', end='')
        for h in range(N):
            print(arr[h][y], end='')

        x += 1
        y -= 1
