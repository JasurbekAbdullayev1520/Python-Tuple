words = ("apple", "banana", "strawberry", "kiwi")

uzun = words[0]   

for word in words:   
    if len(word) > len(uzun): 
        uzun = word      

print(uzun)
