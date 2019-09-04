import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, (input().split()))
    arr = [list(map(str, input())) for n in range(N)]

    for i in range(N):      # N = 글자판 크기
        for j in range(N-M+1):   # N-M+1 = 한 행/열에서 회문 검색 횟수 ()
            # 가로축
            if arr[i][j] == arr[i][j+M-1]:  # 제일 앞문자 == 뒷문자: 검색 시작
                count = 0     # 회문 판별을 위한 카운트 생성
                for x in range(M//2):  # 길이의 절반만 반복
                    # 대치 되는 숫자와 비교
                    # (문자 길이 인덱스 0부터 x를 순차적으로 더해서
                    # 그값에 M-1을 더하고 2*x를 빼면 대치하는 값)
                    if arr[i][j+x] == arr[i][j+x+(M-1)-(2*x)]:
                        count += 1
                    else:   # 틀리면 바로 for문 탈출
                        break
                if count == M//2:
                    print('#{}'.format(t), end=' ')
                    print(''.join(arr[i][j:j+M]))

            # 세로축
            if arr[j][i] == arr[j+M-1][i]:
                count = 0
                for y in range(M//2):
                    if arr[j+y][i] == arr[j+y+(M-1)-(2*y)][i]:
                        count += 1
                    else:
                        break
                if count == M//2:
                    print('#{}'.format(t), end=' ')
                    for m in range(j, j+(M)):
                        print(arr[m][i], end='')
                    print()
