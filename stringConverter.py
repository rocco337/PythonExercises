def toStr(input,base):
    numbers = "0123456789"
    
    if input < base:
        return numbers[input]
    else:
        return toStr(input//base,base) + numbers[input%base]

print toStr(6,2)
print toStr(12456,2)
