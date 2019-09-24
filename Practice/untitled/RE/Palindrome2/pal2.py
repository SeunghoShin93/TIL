import sys
sys.stdin = open('input.txt', 'r')

# T = 10

# N = int(input())

# arr = [list(map(str, input())) for _ in range(100)]

# for i in range(100):
#     for j in range(100):
# -------------------------------

# for t in range(1, 11):
#     T = int(input())
#     arr = [list(map(str, input())) for a in range(100)]
#     count = 0
#     for i in range(100):  # 열 100번 반복
#         for j in range(2, 100):  # 찾는 회문 길이 2~100
#             for k in range(100-j):  # 시작점
#                 result = 0
#                 for l in range(j//2):  # 회문 판별
#                     if arr[i][k+l] == arr[i][k+l+(j-1)-(2*l)]:
#                         result += 1
#                     else:
#                         break
#                 if result == j//2:
#                     if j > count:
#                         count = j

#     print('#{} {}'.format(T, count))

for t in range(1, 11):
    T = int(input())
    arr = [list(map(str, input())) for a in range(100)]
    count = 0
    for i in range(100):  # 열 100번 반복
        for j in range(2, 100):  # 찾는 회문 길이 2~100
            for k in range(100-j):  # 시작점
                # 가로축
                x_result = 0
                y_result = 0
                for l in range(j//2):  # 회문 판별
                    if arr[i][k+l] == arr[i][k+j-1-l]:
                        x_result += 1
                    if arr[k+l][i] == arr[k+j-1-l][i]:
                        y_result += 1

                if x_result == j//2:
                    if j > count:
                        count = j

                if y_result == j//2:
                    if j > count:
                        count = j

    print('#{} {}'.format(T, count))