# def hello():
#     print('Hi!')

name = 'Tyler'

def hello(name):
    global name
    name = 'jess'
    print('Hi {}'.format(name))

hello(name)
