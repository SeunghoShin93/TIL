import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 0
    for i in range(9):
        numbers = []
        numbers2 = []
        for j in range(9):
            if arr[i][j] in numbers:
                break
            if arr[i][j] not in numbers:
                numbers.append(arr[i][j])
            if arr[j][i] in numbers2:
                break
            if arr[j][i] not in numbers2:
                numbers2.append(arr[j][i])
        else:
            result += 1
    if result != 9:
        print('#{} 0'.format(t))
        continue

    x, y = 0, 0
    E = 0
    while x <= 6 and y <= 6:
        numbers = []
        for i in range(3):
            for j in range(3):
                if arr[x+i][y+j] in numbers:
                    E += 1
                else:
                    numbers.append(arr[x+i][y+j])
        if E:
            print('#{} 0'.format(t))
            break
        else:
            if x == 6:
                x = 0
                y += 3
            else:
                x += 3

    if E == 0:
        print('#{} 1'.format(t))
