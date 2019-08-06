import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for x in range(1, T):
    N, K = map(int, input().split())

    for i in range(1, 1 << N+1):
        Sum = 0
        Count = 0
        for j in range(1, N+1):
            if i & (1 << j):
                Sum += j
        if Sum == K:
            Count += 1

    if Count:
        print(Count)
    else:
        print(0)
    #         print(j, end=' ')
    # print()
