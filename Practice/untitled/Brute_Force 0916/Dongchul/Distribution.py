import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visit = [0] * N
    order = []
    result = 1

    lista = []

    def perm(k, n):
        global result
        if k == n:
            for i in range(N):
                result *= arr[i][order[i]]/100
            lista.append(round(result*100, 6))
            result = 1
            return

        for i in range(n):
            if visit[i]:
                continue
            visit[i] = 1
            order.append(i)
        
            perm(k+1, n)
            order.pop()
            visit[i] = 0

    perm(0, N)

    print('#{} {:.6f}'.format(t, round(max(lista), 6)))