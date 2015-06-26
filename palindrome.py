from Deque import Deque

def isPalindrome2(input):
    deque = Deque()
    
    for char in input:
        deque.addRear(char)
    
    isStillEqual = True
    while deque.size()>1 and isStillEqual:
        isStillEqual = deque.removeFront() == deque.removeRear()
            
    return isStillEqual
    

def isPalindrome(input):
    array = []
    for char in input:
        array.append(char)
        
    j= len(array)-1
    i=0
    isStillEqual = True
    while len(array)>1 and isStillEqual:
        if array[i]!=array[j]:
            isStillEqual=False
            
        i=i+1
        j=j-1
    
    return isStillEqual


print(isPalindrome("radar"))
print(isPalindrome('radarr'))
print(isPalindrome('rradar'))
print(isPalindrome('raar'))