def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1  
    if n < 2:
        return n
    return fib(n-1)+fib(n-2)


def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
    

