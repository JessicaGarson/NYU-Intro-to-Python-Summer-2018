import datetime

time = datetime.datetime.now()  # global
name = 'Rachel'


def greeting(time):
    global name
    name = 'Jess'
    print('Hello {}, the time is {}'.format(name, time))


print(name)
greeting(time=time)
print(name)
