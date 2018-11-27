print("Program do rysowania prostokąta o zadanych rozmiarach.")

szerokosc = int(input("Podaj szerokość prostokąta: "))
wysokosc = int(input("Podaj wysokość prostokąta: "))


print("+" + ("-" * szerokosc) + "+")
print(('|' + (" " * szerokosc) + '|\n')*wysokosc, end='')
print("+" + ("-" * szerokosc) + "+")



