arr1 = '()()((()))'


for ch in arr1:
    if ch == '(':
        push(ch)
    else:
        if isEmpty():
            #잘못된 표현
            break
        if ')' and pop() != '(':
            break