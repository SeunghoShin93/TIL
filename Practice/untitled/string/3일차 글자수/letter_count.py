# T = int(input())

pattern = str(input())
text = str(input())

M = len(pattern)
N = len(text)
result = [0]*M

for i in text:
    for j in range(N):
        if i == text[j]:
            result[j] += 1
print(result)
