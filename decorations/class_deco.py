class Decorations(object):
    def __init__(self,func):
        self.func = func
    
    def __call__(self):
        print('Hello i am decarations')
        self.func()

@Decorations
def foo():
    print('i am foo')


foo()