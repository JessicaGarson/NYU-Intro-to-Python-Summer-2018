handles = {'Micheal': 'michealshore93',
           'Daniel': 'danielrein', 'Andrew': 'andyscneider85'}

# for key in sorted(handles.keys()):
#     print('{} is a student in our class'.format(key))

# print(handles.values())
#
# print(handles.items())

# for key, value in handles.items():
#     print('{} is the key for the value {}'.format(key, value))


handles['Alex'] = 'alexng89'
print(handles)

handles.update({'Sara': 'newhandle', 'jess': 'JessicaGarson'})
print(handles)

del handles['Andrew']
print(handles)

handles.clear()
print(handles)
