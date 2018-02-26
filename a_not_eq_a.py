import threading

''' when is a != a ? '''
a = 1
a_ne_a = 0  # count when a != a
n = 10000000

def change_a():
    ''' change a n times '''

    global a
    for i in range(n):  # set a to 0 to n-1
        a = i

t = threading.Thread(target=change_a)
t.start()  # start changing a

for _ in range(n):
    if a != a: # always false?
        a_ne_a += 1
    
t.join()  # wait for change_a to complete

print(f'\na!=a was true {a_ne_a} out of {n} times\n')
