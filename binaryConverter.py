from stack import Stack

def num2Binary(decNumber):
    s = Stack()
        
    while decNumber>0:
        rem = decNumber % 2
        s.push(rem)
        decNumber = decNumber // 2
    
    binString = ""
    while not s.isEmpty():
        binString = binString + str(s.pop())

    return binString

def binary2num(input):
    result = Stack()
    
    index =len(str(input))-1
    for i in str(input):
        result.push(int(i)*(2**index))
        index = index-1
    
    converted = 0
    while not result.isEmpty():
        converted = converted + result.pop()

    return converted
    
print(num2Binary(17))
print(binary2num(10001))
print("-----------------")
print(num2Binary(42))
print(binary2num(101010))