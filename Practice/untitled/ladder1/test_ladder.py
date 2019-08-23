import sys
sys.stdin = open("test_input.txt", "r")

arr = [list(map(int, input().split())) for i in range(8)]
print(arr)
j = 7
x = 0
for i in range(8):
    if arr[j][i] == 2:
        j -= 1
        x = i
    else:
        continue

while j != 0:

    if arr[j][x-1] == 1:
        while arr[j][x-1] == 1:
            x -= 1
    elif arr[j][x+1] == 1:
        while arr[j][x+1] == 1:
            x += 1
    elif arr[j-1][x] == 1:
        while arr[j-1][x] == 1:
            j -= 1
print(x)
