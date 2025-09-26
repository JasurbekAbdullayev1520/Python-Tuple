orders = [(102,"Ali"), (99, "Vali"), (150, "Sami")]
juftlar = []
for i in orders:
    if i[0]%2 == 0:
        juftlar.append(i)
print(juftlar)