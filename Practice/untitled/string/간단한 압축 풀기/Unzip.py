import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    string = ''
    print('#{}'.format(t))
    N = int(input())
    for n in range(N):
        alpha, number = map(str, input().split())
        string += alpha*int(number)

    for i in range(len(string)):
        print(string[i], end='')
        if (i+1) % 10 == 0:
            print()
    # list.append(alpha*int(number))
# for m in range(len(list)):
#     if (m+1) % 10 == 0:
#         print()
#     print(list[m], end='')
