import sys
sys.stdin = open("sample_input.txt", "r")


# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = list(map(int, input().split()))
#     arr = list(map(int, input().split()))
#
#     for m in range(len(arr)-1):
#         if N[0] < arr[m + 1] - arr[m]:
#             result = 0
#             break
#         elif N[0] < arr[0]:
#             result = 0
#             break
#         else:
#             result = N[1] // N[0]
#     print('#{} {}'.format(test_case, result))

"""
고정 변수
K: 1회 이동가능거리 N: 총 이동해야할거리 M: 충전소 개수

설정 변수
Charged : 충전 횟수 

0부터 N+1 for 문을 이동한거리 i
 1회 돌때마다 N-1  K-1     
i in arr


한칸 반복
for x(위치) in N-1:
    K-1
    

"""


T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))



