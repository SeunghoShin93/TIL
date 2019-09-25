import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())

    arr = list(map(int, input().split()))
    visit = [0] * N
    order = []
    ans = B**2

    for R in range(1, N+1):

        def perm(k, s):
            global ans
            if k == R:
                if sum(order) < B:
                    return
                else:
                    if ans > sum(order):
                        ans = sum(order)
                return

            for i in range(s, N):
                order.append(arr[i])
                perm(k+1, i + 1)
                order.pop()
        perm(0, 0)
    print('#{} {}'.format(t, ans-B))
