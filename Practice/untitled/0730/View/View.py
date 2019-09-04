import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

print(N, arr)

def my_max(*args):
    maxnum = 0
    for num in args:
        if num > maxnum:
            maxnum = num
    return maxnum


for n in range(2, N-2):
    result = 0
    MAX = my_max(arr[n - 2], arr[n - 1], arr[n + 1], arr[n + 2])
    if MAX < arr[n]:
        result += arr[n] - MAX




#  주어진 가로길이로 인덱스 번호를 부여해서 n번호 위치 기준 n-1, n-2, n+1, n+2 에 n의 값 미만인 값이 와야 조건이 충족된다.
# 구하는 값 = n의 값에서  n-1 n-2 n+1 n+2 중 최대값을 뺀 값을 모두 더한 값.