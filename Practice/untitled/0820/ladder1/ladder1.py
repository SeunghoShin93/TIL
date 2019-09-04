import sys
sys.stdin = open("input.txt", "r")


# for t in range(1, 11):
T = int(input())
arr = [list(map(int, input().split())) for i in range(100)]

j = 99
x = 0
for i in range(100):
    if arr[j][i] == 2:
        j -= 1
        x = i
        break

while j != 0:

    if arr[j][x-1]:
        while arr[j][x-1] == 1 or x == 1:
            x -= 1
        j -= 1
    elif arr[j][x+1]:
        while arr[j][x+1] == 1 or x == 99:
            x += 1
        j -= 1

    else:
        while arr[j][x-1] == 0 and arr[j][x+1] == 0:
            j -= 1
            continue
print(x)


# i = 0
#
# for j in range(100):
#     if arr[i][j] == 0:
#         continue
#     visit.append(j)
#     while i <= 100:
#         if arr[i][j] == 2:
#             print(visit)
#         if arr[i][j] == 1:
#             if j != 100:
#                 if arr[i][j+1] == 1:
#                     j += 1
#                 else:
#                     i += 1
#
#             if j != 0:
#                 if arr[i][j-1] == 1:
#                     j -= 1
#                 else:
#                     i += 1


# for j in range(100):
#     i = 0
#     visit.append(j)
#     while arr[i][j] != 2:
#         if arr[i][j] == 0:
#             continue
#         elif arr[i][j] == 1:
#             if i != 0:
#                 if j < 99:
#                     if arr[i][j+1] == 1:
#                         j += 1
#                         continue
#                     else:
#                         i += 1
#                         continue

#                 if j > 0:
#                     if arr[i][j-1] == 1:
#                         j -= 1
#                         continue
#                     else:
#                         i += 1
#                         continue
#             else:
#                 i += 1
#                 continue
#     print(visit)
