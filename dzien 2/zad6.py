print("Program do przeliczania liczb w systemie binarnym na dziesiątkowy")

liczba_bin = input("Podaj liczbę w formacie binarnym i 5 indeksach: ")

liczba_dzies = (int(liczba_bin[0]) * (2**5)) + (int(liczba_bin[1]) * (2**4)) + (int(liczba_bin[2]) * (2**3)) + (int(liczba_bin[3]) * (2**2)) + (int(liczba_bin[4]) * (2**1)) + (int(liczba_bin[5]) * (2**0))

print("Twoja liczba w formacie dziesiętnym to: " + str(liczba_dzies))

