import sys
sys.stdin = open("sample_input.txt", "r")


Testcase_number = int(input())


for m in range(1, Testcase_number + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []
    for n in range(N):
        MAX = arr[0]
        MIN = arr[0]
        for number in arr:
            if number > MAX:
                MAX = number
            elif number < MIN:
                MIN = number
    print('#{} {}'.format(m, MAX-MIN))