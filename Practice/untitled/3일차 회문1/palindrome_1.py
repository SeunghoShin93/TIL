import sys
sys.stdin = open("input.txt", "r")

T = 10
# for t in range(1, T+1):
P = int(input())

arr = [list(map(str, input())) for num in range(8)]
r_count = 0
for i in range(8):
    for j in range(9-P):
        x_count, y_count = 0, 0
        for x in range(P//2):
            if arr[i][j+x] == arr[i][j+x+(P-1)-(2*x)]:
                x_count += 1
            if arr[j+x][i] == arr[j+x+(P-1)-(2*x)][i]:
                y_count += 1
            if x_count == P//2:
                r_count += 1
            if y_count == P//2:
                r_count += 1
print(r_count)
