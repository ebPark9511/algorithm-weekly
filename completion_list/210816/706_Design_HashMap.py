class Node: 
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = Node(None, None)

    def append(self, key, value):
        node = self.head
       
        while node.next:
            if node.next.key == key:
                node.next.value = value
                return
            node = node.next

        node.next = Node(key, value)

    def get(self, key):
        node = self.head
        
        while node:
            if node.key == key:
                return node.value
            
            node = node.next

        return None

    def delete(self, key):
        node = self.head

        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                del(node)
                return
            node = node.next

    def search(self):
        print("------search------")
        node = self.head
        while node:
            print(node.value)
            node = node.next            

class MyHashMap:
    
    def __init__(self):
        self.size = 1000
        self.table = [SingleLinkedList() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size     

    def put(self, key: int, value: int):
        index = self._hash(key)
        self.table[index].append(key, value)
            
    def get(self, key: int) -> int:
        index = self._hash(key)
        value = self.table[index].get(key)
        self.table[index].search()        

        if value != None:
            return value
        return -1

    def remove(self, key: int):
        index = self._hash(key)
        self.table[index].delete(key)

hashmap = MyHashMap()
hashmap.remove(2)
hashmap.put(3,11)
hashmap.put(4,13)
hashmap.put(15,6)
hashmap.put(6,15)
hashmap.put(8,8)
hashmap.put(11,0)
print("get: ",hashmap.get(11))
hashmap.put(1,10)
hashmap.put(12,14)


