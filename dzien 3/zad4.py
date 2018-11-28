#Program do wyliczenia wieku psa

wiek_psa = float(input("Podaj wiek psa: "))

if wiek_psa <= 2.0:
    ludzki_wiek_psa = float(wiek_psa)*10.5
    print("Ludzki wiek psa to: " + str(ludzki_wiek_psa))
elif wiek_psa > 100.0:
    print("Pies tyle nie żyje!")
elif wiek_psa > 2.0:
    ludzki_wiek_psa = (2*10.5 + (float(wiek_psa) - 2)*4)
    print(str(ludzki_wiek_psa))
elif wiek_psa > 100.0:
    print("Pies tyle nie żyje!")
