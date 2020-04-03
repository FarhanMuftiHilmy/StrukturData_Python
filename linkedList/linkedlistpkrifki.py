# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
    
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
        self.head = None
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def insertFirst(self, data):
        nodeBaru = Node(data)
        nodeBaru.setNext(self.head)
        self.head = nodeBaru
            
    def deleteFirst(self):
        if self.isEmpty():
            return None
        else:
            yangKeluar = self.head
            self.head = yangKeluar.getNext()
            return yangKeluar
        
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
        if self.isEmpty():
            return None
        elif self.head.getNext()==None:
            yangKeluar = self.head
            self.head = None
            return yangKeluar
        else:
            p = self.head
            while p.getNext().getNext() != None:
                p = p.getNext()
            
            yangKeluar = p.getNext()
            p.setNext(None) #sama dengan p.next = None
            return yangKeluar
        
    def printAll(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.getNext()
               
        
        
LL = LinkedList()
LL.insertFirst("Nussa")
LL.insertFirst("Rara")
LL.insertLast("Anta")
LL.printAll()
print("---------")
LL.deleteFirst()
LL.printAll()
print("---------")
LL.deleteLast()
LL.printAll()
print("---------")
LL.deleteLast()
LL.printAll()
print("---------")
