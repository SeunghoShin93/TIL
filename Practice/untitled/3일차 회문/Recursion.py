# 1, n = 1 or 0
#(n-1)! * n, n> 1

def factorial(n): # 매개변수 - 문제 (크기)를 나타내는 값
                    # 반환값 - n!의 값 (문제의 해)
    if n == 0 or n == 1:    # 기저 사례
        # 재귀호출 하지 않고 종료
        return 1
    else:
        # 재귀호출
        return factorial(n-1) * n

print(factorial(4))
# 1, n = 1 or 0
# (n - 1)! *n, n > 1
