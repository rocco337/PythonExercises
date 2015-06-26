def minFinder(list):
    min = list[0]
    
    for i in list:
        if i < min:
            min = i
        
    print(min)
    
    
minFinder([2,5,6,9,11,158,6,3,-45])