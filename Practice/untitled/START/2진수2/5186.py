import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

N = str(input())
M = N[2::]

# for i in range(len(M)):
#     print(int(M[i])*2**(-(i+1)))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(12))
