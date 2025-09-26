emails = (("Ali", "ali@gmail.com"), ("Vali", "vali@yandex.ru"), ("Sami", "sami@mail.ru"))

domens = set()

for i in emails:
    domen = i[1].split('@')[1]
    domens.add(domen)

print(domens)