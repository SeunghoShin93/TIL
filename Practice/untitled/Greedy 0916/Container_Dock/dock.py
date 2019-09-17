import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())

N = int(input())

arr = [list(map(int, input().split())) for n in range(N)]


def selectionSort(lst):
    for i in range(0, len(lst)-1):
        min = i
        for j in range(i+1, len(lst)):
            if lst[min][0] > lst[j][0]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]


selectionSort(arr)


def Planner(k, lst):
    result = []
    if k == len(lst):
        return result
    else:
        for i in range(k+1, len(lst)):
            if lst[k][1] <= lst[i][0]:
                result.append(lst[i])
                break
            Planner(k+1, lst)
