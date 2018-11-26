print("Program do przeliczania liczb w systemie binarnym na dziesiątkowy")

liczba_bin = int(input("Podaj liczbę w formacie binarnym i 5 indeksach: "))
liczba_dzies = (liczba_bin[0] * (2**5)) + (liczba_bin[1] * (2**4)) + (liczba_bin[2] * (2**3)) + (liczba_bin[3] * (2**2)) + (liczba_bin[4] * (2**1)) + (liczba_bin[5] * (2**0))

print("Twoja liczba w formacie dziesiętnym to: " + liczba_dzies)
