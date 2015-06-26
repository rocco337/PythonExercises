class Node():
    def __init__(self,initData):
        self.data = initData
        self.next = None
    
    def getData(self):
        return self.data
        
    def getNext(self):
        return self.next
        
    def setData(self,data):
        self.data= data
        
    def setNext(self,next):
        self.next = next
        
class UnorderedList():
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head ==None
        
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
        counter=0
        current = self.head
        while current !=None:
            counter = counter+1
            current = current.getNext()
        
        return counter
    
    def search(self,item):  
        isFound = False;
        current = self.head
        while current!=None and not isFound:
            if current.getData() == item:
                isFound = True 
            else:
                current = current.getNext()
            
        return isFound
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))