import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    multi = []

    for i in range(N-1):
        for y in range(i+1, N):
            multi.append(arr[i]*arr[y])

    MAX = 0

    for number in multi:
        if number < 12 or int(str(number)[-1]) == 0 or int(str(number)[-1]) == 1 or int(str(number)[0]) == 9:
            continue
        for j in range(len(str(number))-1, 0, -1):
            if int(str(number)[j-1]) > int(str(number)[j]):
                break
        else:
            if int(str(number)[0]) < int(str(number)[-1]):
                if number > MAX:
                    MAX = number
    if MAX:
        print('#{} {}'.format(t, MAX))
    else:
        print('#{} -1'.format(t))
