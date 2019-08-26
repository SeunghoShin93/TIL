import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
arr = [list(map(int, input().split())) for _ in range(100)]


for i in range(100):
    stack = []
    for j in range(100):
        if arr[j][i] == 1:
            stack.append()
