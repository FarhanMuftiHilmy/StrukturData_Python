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
    def __init__(self, data):
        self.data = data;
        self.next = None;
        
    def getData(self):  
        return self.data
    def getNext(self):
        return self.next
    def setNext(self, newNext):
        self.next = newNext
    def setData(self, newData):
        self.data = newData

class LinkedList:
    def __init__(self):
        self.head = None;
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def insertFirst(self, data):
         nodeBaru = Node(data)
         nodeBaru.setNext(self.head)
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
    def deleteNode(self, data):
        prev = None
        p = self.head
        while p:
            if p.getData() == data:
                if prev:
                    prev.setNext(p.getNext())
                else:
                    self.head = p.getNext()
                    return True
            prev = p
            p = p.getNext()
            
        return False
    
    def printAll(self):
        p = self.head
        #Lakukan selama p-nya tidak None
        while p is not None:
            print(p.data)
            p = p.getNext()
        

LL = LinkedList()
LL.insertFirst('farhan')
LL.insertFirst('hilmy')
LL.insertFirst('Kemal')
LL.insertFirst('Thaha')
LL.printAll()
print("---Count Node-----")
print(LL.countNode())
print("---Cek Data : Kemal-----")
print(LL.cekData('Kemal'))
print("---Cari Data : hilmy-----")
print(LL.cariData('hilmy'))
print("---Sisipkan data Mufti setelah Thaha-----")
LL.sisip('Thaha','Mufti')

LL.printAll()
print("----------")
LL.deleteNode('Mufti')
LL.printAll()


