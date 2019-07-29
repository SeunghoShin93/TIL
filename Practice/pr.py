
# for i in range(n - 1):
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i+1], arr[i]


# print(arr)

# for i in range(n - 2):
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i+1], arr[i]

# print(arr)

# for j in range(n - 1, 0, -1):
#     for i in range(n - 1):
#         if arr[i] > arr[i + 1]:
#             arr[i], arr[i + 1] = arr[i+1], arr[i]

# print(arr)


# 선택정렬

# MIN = arr[0]

# for i in range(1, len(arr)):
#     if arr[i] < MIN:
#         MIN = arr[i]

# print(MIN)
arr = [55, 7, 78, 12, 48]
n = len(arr)


for j in range(len(arr) - 1):
    MIN = 0
    for i in range(j + 1, len(arr)):
        if arr[i] < arr[MIN]:
            MIN = i
    arr[j], arr[MIN] = arr[MIN], arr[j]
print(arr)


# MIN = 1
# for i in range(MIN + 1, len(arr)):
#     if arr[i] < arr[MIN]:
#         MIN = i

# arr[1], arr[MIN] = arr[MIN], arr[1]
# print(arr)
