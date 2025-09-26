students = [("Ali", ["Fizika", "Matematika"]), ("Laylo", ["Ingliz tili"]), ("Jasur", ["Matematika", "Informatika"])]

soni = 0  

for student in students:  
    fanlar = student[1]        
    if "Matematika" in fanlar: 
        soni += 1              

print(f"{soni} talaba Matematika fanini tanlagan.")
