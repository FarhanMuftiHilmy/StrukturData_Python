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
        print("ERROR: STACK KOSONG")
    else:        
        Q.pop(0)
        cetak(queue)
def powenqueue(q, y, x):
    for i in range(y):
        enqueue(q, x)

def powdequeue(q, y):
    if len(q) > y:
        for i in range(y):
            q.pop(0)
        cetak(queue)
    else:
        q.clear()
        print("ERROR: STACK KOSONG")
        
def cetak(Q):
    d = "[ "
    for i in range(len(Q)):
        d = d+Q[i]+" "
    d = d+"]"
    print(d)
    
queue = createNew()
n = int(input())
for i in range(n):
    masuk = input()
    m = masuk.split(" ")
    if m[0] == "enqueue":
        enqueue(queue, m[1])
        cetak(queue)
    elif m[0] == "dequeue":
        dequeue(queue)
    elif m[0] == "powenqueue":
        powenqueue(queue, int(m[1]), m[2])
        cetak(queue)
    elif m[0] == "powdequeue":
        powdequeue(queue, int(m[1]))
        
