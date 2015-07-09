def fibonacciSequence(list,length):
    
    if len(list)>length:
        return list
    
    lastIndex =len(list)-1
    nextNumber = list[lastIndex]+list[lastIndex-1]
    list.append(nextNumber)
    
    return fibonacciSequence(list,length)
    
    
print fibonacciSequence([0,1],28)
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]