import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    if t > 1:
        print()
    N = int(input())

    arr = [[] for _ in range(N)]

    for n in range(N):
        for _ in range(n+1):
            arr[n].append(1)

    for i in range(len(arr)):
        if len(arr[i]) >= 3:
            for j in range(1, len(arr[i])-1):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print('#{}'.format(t))
    for ar in arr:
        if len(ar) > 1:
            print()
        for a in ar:
            print(a, end=' ')
