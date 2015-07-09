def revert(list,index):
    
    if index>=len(list)-1:
        return list
    
    item = list.pop(-1)
    list.insert(index,item)
  
    return revert(list,index+1)
    
print revert(list('roko'),0)
