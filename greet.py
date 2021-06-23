def greet(name):
    ''' prints a greeting to the name variable .'''
    print('hello ' + name)

#greet('Sean') 

def name_input():
    ''' Asks user for their name and then returns said name. '''
    name = input('Please enter your name\n')
    return name


greet(name_input())