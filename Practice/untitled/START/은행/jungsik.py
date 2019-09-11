import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    A = str(input())
    B = str(input())

    a1 = len(A) - 1
    b1 = len(B) - 1

    x = 0
    i = 0
    while a1 >= 0:
        x += int(A[i]) * (2**a1)
        a1 -= 1
        i += 1

    y = 0
    j = 0
    while b1 >= 0:
        y += int(B[j]) * (3**b1)
        b1 -= 1
        j += 1

    for i in range(len(A)):
        S = 0
        if A[i] == '1':
            S = x - (2**(len(A)-1-i))
        if A[i] == '0':
            S = x + (2**(len(A)-1-i))

        S2 = 0
        result = 0
        for j in range(len(B)):
            if B[j] == '2':
                for j2 in range(1, 3):
                    S2 = y - (3**(len(B)-1-j) * j2)
                    if S == S2:
                        print('#{} {}'.format(t, S))
                        result += 1
                        break
            if result:
                break
            if B[j] == '1':
                S2 = y - (3**(len(B)-1-j))

                if S == S2:
                    print('#{} {}'.format(t, S))
                    result += 1
                    break
                S2 = y + (3**(len(B)-1-j))

                if S == S2:
                    print('#{} {}'.format(t, S))
                    result += 1
                    break
            if result:
                break
            if B[j] == '0':
                for j2 in range(1, 3):
                    S2 = y + (3**(len(B)-1-j) * j2)

                    if S == S2:
                        print('#{} {}'.format(t, S))
                        result += 1
                        break
            if result:
                break
