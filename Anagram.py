def anagramSolution1(s1,s2):
    alist = list(s2)
    
    pos1=0
    stillOk = True
    
    #check input lenght before
    
    while pos1<len(s1) and stillOk:
        pos2=0
        found = False
        
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]: 
                found= True
            else:
                pos2 =pos2+1
                
        if found:
            alist[pos2] = None
        else:
            stillOk = False
            
        pos1 = pos1 +1
        
    return stillOk
    
def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)
    
    #still does iterations
    alist1.sort()
    alist2.sort()
    
    pos1=0
    found = True;
    
    while pos1 < len(alist1) and found:
        if alist1[pos1] != alist2[pos1]:
            found = False
        else:
            pos1 = pos1 +1
    
    return found
    
def anagramSolutuion3(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    
  
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos]+1
        
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos]+1
    
    j = 0
    stillOk = True
    while j<26 and stillOk:
        if c1[j] == c2[j]:
            j=j+1
        else:
            stillOk = False
            
    return stillOk
        
    
    
    
print(anagramSolutuion3('aaaadsfad','dasbgbgg'))
print(anagramSolutuion3('heart','earth'))
print(anagramSolutuion3('heart','earth'))