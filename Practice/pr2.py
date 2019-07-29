data = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0]*5  # 최대값 = 4


for val in data:
    counts[val] += 1

sorted = []
for i in range(len(counts)):
    for j in range(counts[i]):
        sorted.append(i)
print(sorted)


for i i n range(1, len(counts)):
    counts[i] = counts[i - 1] + counts[i]
