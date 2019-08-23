import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    stack = []

    arr = list(map(str, input()))

    for alphabet in arr:
        if stack:
            if stack[-1] == alphabet:
                stack.pop()
                continue
        stack.append(alphabet)

    print('#{} {}'.format(t, len(stack)))
