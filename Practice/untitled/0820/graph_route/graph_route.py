import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    listA = []
    for e in range(E):
        start_point, end_point = map(int, input().split())
        listA.append([start_point, end_point])

    N, M = map(int, input().split())

    listB = []

    for i in range(len(listA)):
        if listA[i][1] == M:
            listB.append(listA[i][0])

    result = 0

    for x in listA:
        if listB[0] == x[1]:
            listB.append(x[0])

        if x[0] == N:
            result += 1
            break
        listB.pop(0)
        if result:
            break
    print(result)

# 1. listB - M을 endpoint로 갖는 인자들을 추가
# 2. 인자들에 대하여 startpoint에 N이 있나 조사
# 3. 인자들에 대하여 startpoint를 endpoint로 갖는 인자들 varies 이 있는지 조사 후
# 4. 있다면 그 인자들 삭제 후 varies를 추가
# 5. 없어도 원 인자들 삭제
# 6. 리스트B 유무 조사
