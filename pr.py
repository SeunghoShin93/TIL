# a = 0b1010

# print(a << 1, a << 2, a << 3)
# print(a >> 1)
# print(a >> 2)


# 부분 집합


arr = [3, 6, -2, 7, -3, 1, -5, -1, 5, 4]
N = len(arr)
subset = 10


# for subset in range(1 << N):

#     print(subset, end='>')
#     for j in range(N):
#         if subset & (1 << j):
#             print(arr[j], end=' ')
#     print()


for i in range(1 << N):  # i 는 부분집합
    Sum = 0
    for j in range(N):
        if i & (1 << j):  # arr[j]를 포함하는지
            Sum += arr[j]

    if Sum == 0:
        for j in range(N):
            if i & (1 << j):
                print(arr[j], end=' ')
        print()


# 이진 검색
arr = []
key = 123
low, high = 0, len(arr) - 1


def BinarySearch(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) >> 1   # /2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# 재귀 호출

def BinarySearch2(arr, low, high, key):
    if low > high:
        return False
    mid = (low + high) >> 1   # /2
    if arr[mid] == key:
        return True
    if arr[mid] > key:
        return BinarySearch2(arr, low, mid - 1, key)
    else:
        return BinarySearch2(arr, mid + 1, high, key)


# 선택 정렬

arr = [12, 324, 2, 2, 5, 6]
N = len(arr)
# [0, n-1] 최소값 위치

for i in range(N-1):
    min = i
    for j in range(min + 1, N):
        if arr[min] > arr[j]:
            min = j
    arr[0], arr[min] = arr[min], arr[0]
print(arr)

# min = 1

# for j in range(min +1, N):
#     if arr[min] > arr(j):
#         min = j
# arr[1], arr[min] = arr[min], arr[1]
