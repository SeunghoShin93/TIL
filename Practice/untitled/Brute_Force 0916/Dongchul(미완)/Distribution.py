import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100
    visit = [0] * N
    order = []
    ans = 0

    def perm(k, n, p):
        global ans
        if p <= ans:
            return
        if k == n:
            ans = p
            return

        for i in range(n):
            if visit[i]:
                continue
            visit[i] = 1
            order.append(i)
            perm(k+1, n, p * arr[k][i])
            order.pop()
            visit[i] = 0

    perm(0, N, 100)

    print('#{} {:.6f}'.format(t, round(ans, 6)))
