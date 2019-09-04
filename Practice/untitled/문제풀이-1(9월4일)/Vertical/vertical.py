import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    if t > 1:
        print()
    print('#{}'.format(t), end=' ')
    arr = [list(map(str, input())) for _ in range(5)]
    Maxlength = 0
    for ar in arr:
        if len(ar) > Maxlength:
            Maxlength = len(ar)
    for ar in arr:
        S = Maxlength - len(ar)
        if S > 0:
            for s in range(S):
                ar.append('')

    for i in range(Maxlength):
        for j in range(5):
            print(arr[j][i], end='')
