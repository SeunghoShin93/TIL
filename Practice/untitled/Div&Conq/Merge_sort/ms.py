import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    tmp = [0] * len(arr)
    cnt = 0

    def mergeSort(lo, hi):		# 매개변수 -- > 문제 크기
        global cnt
        if lo == hi:
            return

        mid = (lo + hi - 1) >> 1
        mergeSort(lo, mid)  # 왼쪽
        mergeSort(mid + 1, hi) 	# 오른쪽
        # 왼쪽 오른쪽 병합

        i, j, k = lo, mid + 1, lo
        while i <= mid and j <= hi:
            if arr[i] < arr[j]:
                tmp[k] = arr[i]
                i, k = i + 1, k + 1
            else:
                tmp[k] = arr[j]
                j, k = j + 1, k + 1
        while i <= mid:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        while j <= hi:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1

        if arr[mid] > arr[hi]:
            cnt += 1

        for i in range(lo, hi + 1):
            arr[i] = tmp[i]

    mergeSort(0, len(arr) - 1)

    print('#{} {} {}'.format(t, arr[N//2], cnt))
