import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())

    arr = list(map(int, input().split()))

    for m in range(M):
        change = list(map(str, input().split()))
        if change[0] == 'I':
            arr.insert(int(change[1]), int(change[2]))

        if change[0] == 'D':
            arr.pop(int(change[1]))

        if change[0] == 'C':
            arr[int(change[1])] = int(change[2])

    if L <= len(arr):
        print('#{} {}'.format(t, arr[L]))
    else:
        print('#{} -1'.format(t))
