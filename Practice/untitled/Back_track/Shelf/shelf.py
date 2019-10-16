import sys
sys.stdin = open('input.txt', 'r')


def perm(k, s, p):
    global ans
    x = sum(order)
    if x == B:
        ans = x
        return

    if k == p:
        if ans > x >= B:
            ans = x

        return

    if x > ans:
        return
    for i in range(s, N):
        order.append(arr[i])
        perm(k+1, i + 1, p)
        order.pop()


T = int(input())

for t in range(1, T+1):
    N, B = map(int, input().split())

    arr = list(map(int, input().split()))
    visit = [0] * N
    order = []
    ans = B ** 2

    perm(0, 0, N)
    print('#{} {}'.format(t, ans-B))
