print("Czy dany rok jest rokiem przestępnym?")
rok = int(input("Podaj rok: "))

if (rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0)):
    print("Podany rok jest przestępny.")
else:
    print("Podany rok nie jest przestępny")
