import sys
sys.stdin = open("sample_input.txt", "r")


# 정렬 된 리스트에서


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    aj = list(map(int, input().split()))
    for i in range(0, N - 1):
        min = i
        for j in range(i+1, N):
            if aj[min] > aj[j]:
                min = j
        aj[i], aj[min] = aj[min], aj[i]

    Big = []
    Small = []
    result = []
    for x in range(N):
        if x < len(aj)//2:
            Small.append(aj[x])
        else:
            Big.append(aj[x])

    for i in range(0, len(Small) - 1):
        min = i
        for j in range(i+1, len(Small)):
            if Small[min] < Small[j]:
                min = j
        Small[i], Small[min] = Small[min], Small[i]

    while True:
        if len(Big) == 0 and len(Small) == 0:
            break
        if len(Big):
            result.append(str(Big.pop()))
        if len(Small):
            result.append(str(Small.pop()))

    print(' '.join(result))
