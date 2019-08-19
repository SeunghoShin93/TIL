import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    arr = list(input())

    checklist = []
    #result = 0 
    for par in arr:
        if par == '(' or par == '{':
            checklist.append(par)

        if par == ')':
            if len(checklist) == 0 or checklist[-1] != '(':
                print('#{} 0'.format(t))
                #result += 1
                break
            else:
                checklist.pop()


        if par == '}':
            if len(checklist) == 0 or checklist[-1] != '{':
                print('#{} 0'.format(t))
                #result += 1
                break
            else:   
                checklist.pop()
    else:     
        if checklist:
            print('#{} 0'.format(t))
        else:
            print('#{} 1'.format(t))