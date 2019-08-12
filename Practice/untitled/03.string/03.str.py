import sys
sys.stdin = open("GNS_test_input.txt", "r")

T = int(input())
# for t in range(T):


Q = list(map(str, input().split()))
M = int(Q[1])
numbers = list(map(str, input().split()))
no_list = ["ZRO", "ONE", "TWO", "THR",
           "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for i in range(M):
    for j in range(len(no_list)):
        if numbers[i] == no_list[j]:
            numbers[i] = j


print(numbers)
