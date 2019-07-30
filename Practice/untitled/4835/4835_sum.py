import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))


    result = []

    for i in range(len(arr)-M+1):
        a = 0
        for x in range(i, i+M):
             a += arr[x]
        result.append(a)
    #print(result)
    Max = result[0]
    Min = result[0]
    for number in result:
        if number > Max:
            Max = number
        if number < Min:
            Min = number
    print('#{} {}'.format(test_case, Max-Min))


"""
구간개수 M
인덱스 i
x = (M+1)

i -x, i -x+1  ,.....  i
i +x, x+x-1   ......  i
구간합 구하는법 

for i in range(
range(i, i+x+1)
range(i-x, i+1)


리스트에 모든 구간합을 저장한 후
최대값 - 최소값

"""