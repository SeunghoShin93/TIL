def hello(func):
    def wrapper():
        print('HIHI')
        func()
        print('haha')
    return wrapper



@hello    
def bye():
    print('bye')

bye()