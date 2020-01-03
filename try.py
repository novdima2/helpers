L = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(L)
print(L[1])
print(L[2:1])

D = {'x':1, 'y':2, 'z':3}
D[(1,2,3)] = 4
print(D)
D['w']=0
print(D)
print(D['x'] + D['z'])
print ([[[]]])
print ((1,2,3) in D)

del L[::2]
print (L)

while True:
    reply = raw_input('Enter text:')
    if reply == 'stop': break
    print(reply.upper())

