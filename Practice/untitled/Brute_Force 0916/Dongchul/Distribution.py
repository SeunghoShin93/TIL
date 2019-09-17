from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

N = int(input())

arr = [list(map(float, input().split())) for _ in range(N)]

# for n in range(N):
#     for i in range(N):
#         if n == i:
#             continue
#         for j in range(N):
#             if j == n or j == i:
#                 continue
#             for k in range(N):
#                 if k == n or k == i or k == j:
#                     continue

#                 print((arr[n][0] * arr[i][1] *
#                        arr[j][2] * arr[k][3]) / 100**(N-1))


def perm(k, N):
    if k == N:
        print()
    for i in range(N):
        perm(k+1, N)


print(perm(0))
