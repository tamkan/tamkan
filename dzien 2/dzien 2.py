print("Czesc!")

imie = input("Podaj imie: ")
imie = imie.strip(" ")
dlugosc_imienia = len(imie)
ostatnia_litera_imienia = imie[dlugosc_imienia - 1]

print(imie[-1:])

print("Czesc " + imie.capitalize()+ "!")
print("Twoje imie ma: " + str(len(imie)) + " liter")
print("Twoja ostatnia litera to " + '"' + str(ostatnia_litera_imienia) + '"')

if ostatnia_litera_imienia == "a":
    print("Jestes kobieta")
elif ostatnia_litera_imienia != "a":
    print("Jestes mezczyzna")
else:
    print("Nie wiem kim jestes")
#komentarz

