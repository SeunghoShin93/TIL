import sys
sys.stdin = open("input2.txt", "r")

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

            if x_result == l:
                if j > count:
                    print(j)
                    count = j

            for l in range(j//2):
                if arr[k+l][i] == arr[k+j-1-l][i]:
                    y_result += 1

            if y_result == l:

                if j > count:
                    print(j)
                    count = j


print('#{} {}'.format(T, count))
