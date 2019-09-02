import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    stack = []
    operator = ['*', '/', '+', '-']
    arr = list(map(str, input().split()))

    for i in arr:
        if i not in operator:
            stack.append(i)
        else:
            if i == '+':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b)+int(a))
                else:
                    print('#{} error'.format(t))
                    break
            if i == '-':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b)-int(a))
                else:
                    print('#{} error'.format(t))
                    break
            if i == '*':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b)*int(a))
                else:
                    print('#{} error'.format(t))
                    break
            if i == '/':
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b)/int(a))
                else:
                    print('#{} error'.format(t))
                    break
    else:
        if len(stack) == 1:
            print('#{} {}'.format(t, stack[0]))
        else:
            print('#{} error'.format(t))
