import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())

    arr = [list(map(str, input())) for _ in range(N)]

    cnt = [[0] * (_+1) for _ in range(0, N, 2)]

    sum = 0
    for i in range(len(cnt)):
        x = (N - len(cnt[i]))//2
        for j in range(len(cnt[i])):
            sum += int(arr[i][x+j])
            if N-1-i != N//2:
                sum += int(arr[N-1-i][x+j])

    print('#{} {}'.format(t, sum))
