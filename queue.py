def createNew():
    return []
def enqueue(Q, data):
    Q.append(data)
    
def isEmpty(Q):
    if len(Q) == 0:
        return True
    else:
        return False
def dequeue(Q):
    if isEmpty(Q):
        return None
    else:
        #cara 1
        '''
        x = Q[0] 
        for i in range(len(Q)-1):
            Q[i] = Q[i+1] #buat elemen sebelumnya adalah elemen setelahnya
        Q.pop()
        return x
        '''
        # cara 2
        '''
        Q.reverse()
        Q.pop()
        Q.reverse()
        '''
        # cara 3
        return Q.pop(0)
    
def clear(Q):
    Q.clear()
def cetak(Q):
    print(Q)
    
def pownqueue(q, x, y):
    for i in range(y):
        enqueue(q, x)

def powdequeue(q, y):
    for i in range(y):
        dequeue(q)



# EXECUTE !!!!!!!!!!    
queue = createNew()
for i in range(5):
    data = input()
    enqueue(queue, data)

cetak(queue)
dequeue(queue)
dequeue(queue)
enqueue(queue, 7)
cetak(queue)
clear(queue)
cetak(queue)