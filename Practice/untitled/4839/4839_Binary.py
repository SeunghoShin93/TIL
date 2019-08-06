import sys
sys.stdin = open("sample_input.txt", "r")


def BinarySearch(arr, key):
    low, high = 1, arr
    mid = count = 0
    while mid != key:
        mid = (low + high) >> 1
        count += 1
        if mid > key:
            high = mid
        else:
            low = mid
    return count


T = int(input())
for t in range(1, T+1):

    P, Pa, Pb = map(int, input().split())

    if BinarySearch(P, Pa) == BinarySearch(P, Pb):
        print(0)
    elif BinarySearch(P, Pa) < BinarySearch(P, Pb):
        print('A')
    else:
        print('B')
