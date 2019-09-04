import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    if t > 1:
        print()
    N, M, K = map(int, input().split())
    a = M
    arr = list(map(int, input().split()))

    for k in range(K):
        if M > len(arr):
            M %= len(arr)
            x = arr[M-1]
            y = arr[M]
            arr.insert(M, x+y)
        elif M == len(arr):
            x = arr[M-1]
            y = arr[0]
            arr.append(x+y)
        else:
            x = arr[M-1]
            y = arr[M]
            arr.insert(M, x+y)
        M += a
    arr.reverse()
    print('#{}'.format(t), end=' ')
    cnt = 0
    for ar in arr:
        if cnt == 10:
            break
        print(ar, end=' ')
        cnt += 1

#    498 667  2514
#  958 386 715 329 169 778  1736
