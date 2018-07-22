from functools import wraps
def decoration(func):
    @wraps(func)
    def wrapper(*args,**kw):
        print("Hello World")
        return func(*args,**kw)
    return wrapper

@decoration    
def foo():
    print('Hello I am foo')
    
a = foo() # 调用foo
print(foo.__name__)
