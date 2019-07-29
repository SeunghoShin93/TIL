data = [7, 4, 2, 0, 0, 6, 0, 7, 0]


# 모든 상자의 낙폭을 구할필요 X

# 높이 - 밑에있는 상자 개수       높이는 최고 높이, 상자 개수는 최저

# 높이가 같거나 큰 상자를 찾아야함


# 순열만들기
data = 'ABC'

n = len(data)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == k or j == k:
                continue
            print(data[i], data[j], data[k])
