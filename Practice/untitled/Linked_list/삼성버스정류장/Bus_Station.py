import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    if t > 1:
        print()
    print('#{}'.format(t), end=' ')
    N = int(input())
    arr = []
    for n in range(N):
        start, end = map(int, input().split())
        arr.append(start)
        arr.append(end)
    result = [0] * (max(arr)+1)

    while arr:
        a = arr.pop(0)
        b = arr.pop(0)
        for j in range(a, b+1):
            result[j] += 1
    P = int(input())
    for p in range(P):
        x = int(input())
        print(result[x], end=' ')
