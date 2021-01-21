n = input()
s = set(map(int, raw_input().split())) 
a = input()

for i in xrange(a):
    k = []
    k = raw_input().split()
    if k[0] == 'pop':
        s.pop()
    elif k[0] == 'remove':
        s.remove(int(k[1]))
    elif k[0] == 'discard':
        s.discard(int(k[1]))
    else:
        print 'not a command'

 print sum(s)
