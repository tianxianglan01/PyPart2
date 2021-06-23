def exponentiate(a, b):
    '''raises a to the power of b'''
    return a ** b

#print(exponentiate(3,4))

def raise_to_fourth_power(a):
    '''raises a to the fourth power'''
    return exponentiate(a, 4)

#print(raise_to_fourth_power(5))

square = lambda a: exponentiate(a, 2)

#print(square(2))

cube = lambda b: exponentiate(b, 3)

print(square(2))

print(cube(2))

print(raise_to_fourth_power(2))


