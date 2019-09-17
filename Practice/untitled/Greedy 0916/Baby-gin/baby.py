import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))

    A = []
    B = []

    def Check(lst):
        num = [0] * 10
        for number in lst:
            num[number] += 1

        # triplet
        for n in num:
            if n == 3:
                return True
        else:
            # run
            for i in range(8):
                if num[i] >= 1:
                    if num[i+1] >= 1 and num[i+2] >= 1:
                        return True

    for i in range(len(arr)//2):
        A.append(arr.pop(0))
        if len(A) >= 3:
            Check(A)
            if Check(A):
                print('#{} 1'.format(t))
                break
        B.append(arr.pop(0))
        if len(B) >= 3:
            Check(B)
            if Check(B):
                print('#{} 2'.format(t))
                break
    else:
        print('#{} 0'.format(t))
