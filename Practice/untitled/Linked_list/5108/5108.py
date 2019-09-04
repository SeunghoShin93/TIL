import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):

    N, M, L = map(int, input().split())

    arr = list(map(int, input().split()))

    for m in range(M):
        i, x = map(int, input().split())
        arr.insert(i, x)
    print('#{} {}'.format(t, arr[L]))
