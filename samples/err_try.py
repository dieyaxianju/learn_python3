__author__ = 'ASUS'

def some_function():
    r = 10/1
    print(r)
    return r

def foo():
    r = some_function()
    print(r)
    if r==(-1):
        return -1
    return r
def bar():
    try:
        foo()
    except:
        print('error')


