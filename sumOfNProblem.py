from stack import Stack

def sumUp(i,numbers,operator,sum,expression):
    finalSum = 36
    while i<len(numbers):
        sum = sum + numbers[i]
        
        expression = expression + str(numbers[i]) + operator
        print(expression)
        
        i=i+1
        if sum == finalSum:
            return expression
        else:
            sum2 = sumUp(i,numbers,'+',sum,expression)
            if sum2 == finalSum:
                return expression
            

    

params = Stack()
params.items= [1,2,3,4,5,6,7,8,9]

operators = Stack()
print(sumUp(0, [1,2,3,4,5,6,7,8,9],'+',0,''))