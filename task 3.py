a = input('Enter your first number: ')
b = input('Enter youre second number: ')
c = input('Enter your operation: ')

a = int(a)
b = int(b)
#  Арифметичні операції
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    print(a/b)
    
# Операції порiвняння
if c == 'comprasion':
    d = input('Choose comprasion: ')
    if d == '>':
        if a > b:
            print('a more than b')
        
    if d == '<':
        if a < b:
            print('a less than b')
        
    if d == '=':
        if a == b:
            print('a equals b')
        if a != b:
            print('a not equals b')    
    
    
    
    
    
    














