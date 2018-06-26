import datetime


time = datetime.datetime.now()  # global


def greeting(time):
    name = 'Jess'  # local and temporary
    print('Hello {}, the time is {}'.format(name, time))


print(name)
greeting(time=time)
