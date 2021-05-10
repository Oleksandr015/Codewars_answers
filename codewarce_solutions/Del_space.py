from operator import add, sub
d = {'add':add, 'sub':sub}

print((d.get('mul', add)(5,4)))

