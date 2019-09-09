import sys
sys.stdin = open('input.txt', 'r')

passcode = ['0001101', '0011001', '0010011', '0111101', '0100011',
            '0110001', '0101111', '0111011', '0110111', '0001011']


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(str, input())) for _ in range(N)]

    codes = []
    x, y = 0, 0
    end = 0
    a = 56
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                x, y = i, j
                end += 1
                break
        if end:
            break

    while a != 0:
        codes.append(arr[x][y])
        y -= 1
        a -= 1
    codes.reverse()

    result = []

    code = ''
    while codes:
        x = codes.pop(0)
        code += x
        if code in passcode:
            result.append(passcode.index(code))
            code = ''

    odd = []
    even = []

    for j in range(0, 8, 2):
        odd.append(result[j])
        even.append(result[j+1])

    Tresult = sum(odd)*3 + sum(even)

    if Tresult % 10:
        print('#{} 0'.format(t))
    else:
        print('#{} {}'.format(t, sum(odd)+sum(even)))
