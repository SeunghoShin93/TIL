from collections import deque
S = deque()
for i in range(10):
    S.append(i)
while S:
    print(S.pop())