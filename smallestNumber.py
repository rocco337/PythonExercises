def smallestNumber(list):

    min = list[0]
    for i in list:
        min = i if i<min else min
            
    return min
    
print(smallestNumber([10,25,99,8,6,1,-5]))