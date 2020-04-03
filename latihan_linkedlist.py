# -*- coding: utf-8 -*-
"""
LATIHAN!

Buatlah method:
1. def countNode() #jumlah nodenya
2. def cekData(self, mawar) #misal namanya mawar
    return True / False
3. def cariData(self, mawar)
    return urutanKeBerapa,
    kalau tidak ada outputkan -1
4. def sisip(self, mawar,dataBaru)
    #masukkan dataBaru di setelah mawar
    #jika mawar tidak ada insertLast
5. def deleteNode(self, mawar)
    # hapus data = mawar
6. Coba simulasikan penjumlahan polinomial menggunakan LinkedList
"""


class Node:
    #Constructor
    def __init__(self, data):
        self.data = data;
        self.next = None;       
    #SetterGetter
    def getData(self):  
        return self.data
    def getNext(self):
        return self.next
    def setNext(self, newNext):
        self.next = newNext
    def setData(self, newData):
        self.data = newData

class LinkedList:
    #Constructor
    def __init__(self):
        self.head = None;
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def insertFirst(self, data):
         nodeBaru = Node(data)
         #Set self.head jadi self.next nodeBaru dulu
         nodeBaru.setNext(self.head)
         #Setelah itu, baru nodeBaru dijadikan self.head 
         self.head = nodeBaru
        
#==============================================================================
#         if isEmpty():
#             nodeBaru = Node(data)
#             self.head = nodeBaru
#         else:
#             nodeBaru = Node()
#             nodeBaru.setNext(self.head)
#             self.head = nodeBaru
#==============================================================================
    
    def deleteFirst(self):
        if self.isEmpty():
            return None
        else:
            yangkeluar = self.head
            self.head = yangkeluar.getNext()
            return yangkeluar
        
    def insertLast(self, data):
        if self.isEmpty():
            self.insertFirst(data)
        else:
            p = self.head
            while p.getNext() is not None:
                p = p.getNext()
            nodeBaru = Node(data)
            p.setNext(nodeBaru)
                
    def deleteLast(self):
        if self.isEmpty(): #data kosong
            return None
        elif self.head.getNext() == None: #data cuma satu:
            yangkeluar = self.head
            self.head = None
            return yangkeluar
        else :#data lebih dari satu
            p = self.head
            while p.getNext().getNext() is not None:
                p = p.getNext()
            yangkeluar = p.getNext()
            p.setNext(None) #sama dengan p.next = None
            return yangkeluar
        
    def countNode(self):
        jumlah = 0
        p = self.head
        while p is not None:
            jumlah += 1
            p = p.getNext()
        return jumlah
    
    def cekData(self, data):
        p = self.head        
        
        while p is not None:
            if p.getData() == data:
                return True
            p = p.getNext()
        return False
                            
    def cariData(self, data):
        urutanke = 0
        p = self.head
        #return urutan keberapa
        while p is not None:
            urutanke += 1
            if p.getData() == data:
                return urutanke
            p = p.getNext()
        return -1
        
        
    def sisip(self, prevData, newData):
        
        p = self.head
        while p.data is not prevData:
            p = p.getNext()
            if p is None:
                self.insertLast(newData)
                return True   
           
                           
       
        
        newNode = Node(newData)
        dataNext = p.getNext()
        p.setNext(newNode)
        p.getNext().setNext(dataNext)
        
    #nomor 4
    def deleteNode(self, key):
        # Store head node  
        temp = self.head  
  
        # If head node itself holds the key to be deleted  
        if (temp is not None):  
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return # same with break
  
        # Search for the key to be deleted, keep track of the  
        # previous node as we need to change 'prev.next'  
        while(temp is not None):  
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
  
        # if key was not present in linked list  
        if(temp == None):  
            return
  
        # Unlink the node from linked list  
        prev.next = temp.next
  
        temp = None
    
    def printAll(self):
        p = self.head
        #Lakukan selama p-nya tidak None
        while p is not None:
            print(p.data)
            p = p.getNext()
        
print("---Masukkan data dan print semua data-----")
LL = LinkedList()
LL.insertFirst('nama1')
LL.insertFirst('nama2')
LL.insertFirst('nama3')
LL.insertFirst('nama4')
LL.printAll()

print("---Count Node-----")
print(LL.countNode())


print("---Cek Data-----")
print(LL.cekData('nama3'))


print("---Cari Data-----")
print("Data urutan ke -", LL.cariData('nama2'))


print("---Sisipkan data nama sisipan setelah nama3-----")
LL.sisip('nama4','nama-sisipan')

LL.printAll()
print("---Menghapus node tertentu-----")
LL.deleteNode('nama-sisipan')
LL.deleteNode('nama1')

LL.printAll()



