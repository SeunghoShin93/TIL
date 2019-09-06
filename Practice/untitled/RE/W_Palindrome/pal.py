import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):

    arr = list(str(input()))
    N = len(arr)

    # 물음표가 있는지부터 판별
    if '?' in arr:
        for i in range(N//2):
            if arr[i] == '?' and arr[N-i-1] != '?':
                arr[i] = arr[N-i-1]
            if arr[N-i-1] == '?' and arr[i] != '?':
                arr[N-i-1] = arr[i]

    for j in range(N//2):
        if arr[j] == arr[N-j-1]:
            pass
        else:
            print('#{} Not Exist'.format(t))
            break
    else:
        print('#{} Exist'.format(t))
