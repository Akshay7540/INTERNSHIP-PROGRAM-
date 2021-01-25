def print_rangoli(size):
    # your code goes here
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1,-size,-1):
        rangoli = '-'.join(alpha[size-1:abs(i):-1]+alpha[abs(i):size])
        print(rangoli.center(4*size-3,'-'))
        