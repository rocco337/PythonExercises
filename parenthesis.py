from stack import Stack

def parChecker(symbolString):
    s = Stack()
    ii=0
    balanced = True;
    while ii< len(symbolString) and balanced: 
        symbol = symbolString[ii]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        
        ii=ii+1
        
    if s.isEmpty() and balanced:
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)  

print(parChecker('((()))'))
print(parChecker('(()'))
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))