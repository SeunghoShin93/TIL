# C- style
S = [0] * 3
top = -1

def push(item):
    global top
    # full 상태를 체크
    if top == 2: return 'full'
    top += 1
    S[top] = item

def pop():
    global top
    # empty 상태를 체크
    if top == -1: return  'empty'
    ret = S[top]
    top -= 1
    return ret



# python style
def push(item):
    S.append(item)

def pop(): # pop을 할땐 항상 empty 상태 체크
    # empty  상태 체크
    return S.pop()

def isEmpty():
    return len(S) == 0

for i in range(3):
    push(i)

print(pop())
print(pop())