print("Hej!")
print("Witaj w programie, który poda pierwszą i ostatnią cyfrę podanej liczby")

liczba = input("Podaj liczbę: ")

pierwsza_cyfra = liczba[0]
ostatnia_cyfra = liczba[-1]

if liczba.isdigit():
    print("pierwsza cyfra: " + pierwsza_cyfra)
    print("ostatnia cyfra: " + ostatnia_cyfra)
else:
    print("Podaj liczbę, nie literę!")

