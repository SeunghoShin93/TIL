import sys
sys.stdin = open("input.txt", "r")
for i in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    Max = 0
    dsum = dsum2 = 0
    for i in range(100):
        csum = rsum = 0
        dsum += arr[i][i]
        dsum2 += arr[i][99-i]
        for j in range(100):
            csum += arr[i][j]
            rsum += arr[j][i]
        Max = max(Max, dsum, dsum2, csum, rsum)
    # Max= max(Max, )

    print(Max)
