n = int(input())
inputs = list(map(int,input().split()))


# Function to display hashtable 
def display_hash(hashTable): 
      
    for i in range(len(hashTable)): 
        print(i, end = "=") 
          
        for j in hashTable[i]:  
            print(j, end="") 
              
        print() 
  
# Creating Hashtable as  
# a nested list. 
HashTable = [[] for _ in range(5)] 
  
# Hashing Function to return  
# key for every value. 
def Hashing(keyvalue): 
    return keyvalue % len(HashTable)
  
  
# Insert Function to add 
# values to the hash table 
def insert(Hashtable, keyvalue): 
      
    hash_key = Hashing(keyvalue) 
    Hashtable[hash_key].insert(0, keyvalue) 
  
# Driver Code 
for i in range(n):
    insert(HashTable, inputs[i])
  
display_hash(HashTable) 
            




    
    