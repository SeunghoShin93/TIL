# arr = str(input())
# stack = []
# for x in arr:
#     if x not in '+*/-':
#         print(x, end='')
#     else: 
#         stack.append(x)
# while stack:
#     print(stack[-1], end='')
#     stack.pop()


# def backtrack(a, k, input):
#     global MAXCANDIDATE
#     c = [0] * MAXCANDIDATE

#     if k == input:
#         for i in range(1, k+1):
#             print(a[i], end= ' ')
#         print()
#     else:
#         k += 1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k , input)
    
# def construct_candidates(a, k , input, c):
#     in_perm = [False] * NMAX

#     for i in range(1, k ):
#         in_perm[a[i]] = True

#     ncandidates = 0
#     for i in range(1, input+1):
#         if in_perm[i] == False :
#             c[ncandidates] = i 
#             ncandidates += 1
#     return ncandidates
    
def backtrack(a, k, input):
    global MAXCANDIDATES
    c=[0]*MAXCANDIDATES
    if k == input:
        process_solution(a,k)
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

def process_solution(a, k):
   
    Sum = 0
    for i in range(k+1):
      
        if a[i]:
            Sum += i
    if Sum == 10:
        print('(', end='')
        for i in range(k+1):
            if a[i]:
                print(i, end='')
    
        print(')')


def construct_candidates(a, k , input, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 100
NMAX = 100
a = [0]*NMAX
backtrack(a, 0, 10)


# -----------------------------------

def QuickSort(a, begin, end):
    if begin < end:
        pivot = partition(a, begin, end)
        QuickSort(a, begin, p-1)
        QuickSort(a, p+1, end)


def partition(a, begin, end):
    # pivot = (begin+end) // 2
    L = begin
    R = end
    while L < R :
        while (a[L] < a[pivot] and L < R):
            L += 1
        while (a[R] >= a[pivot] and L < R):
            R -= 1
            if L < R:
                if L == pivot:
                    pivot = R
                a[L], a[R] = a[R], a[pivot]
    return R

a = [54, 88, 77, 26, 93, 17, 49]

QuickSort(a, 17, 93)

