try:
    unicode('')
    input = raw_input
except:
    pass

abc = input('What you talkin about Willis? ')
print('-> You said: {0}'.format(abc))
