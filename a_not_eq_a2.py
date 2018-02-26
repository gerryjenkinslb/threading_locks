import threading
''' when is a != a ? '''

a = 1
a_ne_a = 0  # count when a != a
n = 10000000

lock1 = threading.Lock() # get lock
# only one thread can 'hold' the lock at a time
# the other waits for it to be released

def change_a():
    ''' change a n times '''
    global a
    for i in range(n):
        with lock1:  # hold off main thread
            a = i

t = threading.Thread(target=change_a)
t.start()  # start thread running change_a()

for _ in range(n):
    with lock1:  # hold off hold lock for with block
        if a != a: # always false?
            a_ne_a += 1 # count times it is true

t.join()  # wait for change_a thread to complete


print(f'\na!=a was true {a_ne_a} out of {n} times\n')

