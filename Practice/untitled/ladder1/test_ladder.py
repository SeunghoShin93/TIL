import sys
sys.stdin = open("test_input.txt", "r")

arr = [list(map(int, input().split())) for i in range(5)]
visit = []
for j in range(8):
    i = 0
    visit.append(j)
    if arr[i][j] == 2:
        print(visit)
    if arr[i][j] == 0:
        continue
    elif arr[i][j] == 1:
        if i != 0:
            if j < 99:
                if arr[i][j+1] == 1:
                    j += 1
                    continue
                else:
                    i += 1
                    continue

            if j > 0:
                if arr[i][j-1] == 1:
                    j -= 1
                    continue
                else:
                    i += 1
                    continue
        else:
            i += 1
            continue