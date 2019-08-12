import sys
sys.stdin = open("sample_input.txt", "r")


def BruteForce(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M:
        return 1
    else:
        return 0


T = int(input())


for t in range(1, T+1):
    pattern = str(input())
    text = str(input())
    M = len(pattern)
    N = len(text)

    print('#{} {}'.format(t, BruteForce(pattern, text)))
