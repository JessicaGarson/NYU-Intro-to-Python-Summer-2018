import datetime


time = datetime.datetime.now()  # global


def greeting(time):
    name = 'Jess'  # local and temporary
    return('Hello {}, the time is {}'.format(name, time))

# won't work
# print(name)
greet = greeting(time=time)
print(greet)
