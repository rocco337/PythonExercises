def reverse(input):
    length = len(input)
    
    if length==1:
        return input[0];
        
    return input[length-1] + reverse(input[:-1])
    

print(reverse("roko"))
print(reverse("vienna"))