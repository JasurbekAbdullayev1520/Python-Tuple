people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]


eng_katta = people[0]

for person in people:
    if person[1] > eng_katta[1]:  
        eng_katta = person

print(f"Eng katta yoshli odam: {eng_katta[0]} {eng_katta[1]}")
