import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for i in range(T):  # 테스트케이스 개수
    N = int(input())
    listA = []
    listB = []
    for j in range(N):  # 칠할 구간 개수 (색깔 개수)
        arr = list(map(int, input().split()))
        I = arr[2] - arr[0]
        J = arr[3] - arr[1]
        # print(I, J)
        for x in range(I+1):
            for y in range(J+1):
                if arr[-1] == 1:
                    listA.append((arr[0]+x, arr[1]+y))
                else:
                    listB.append((arr[0]+x, arr[1]+y))
    print(listA)
    print(listB)
    print(len(set(listA) & set(listB)))

# arr[-1] == 색깔 번호
# 같은 경우 좌표 더하고
# 다른 경우 &로 교집합
