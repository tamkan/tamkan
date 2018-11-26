print("Hej!")
print("Witaj w programie do obliczania pola powierzchni koła o zadanym promieniu ")

promien_kola = input("Podaj wartość promienia koła: ")

print("Wzór na obliczenie pola powierzchni koła: P = π * (r^2)")
import  math

pi = math.pi

pole_pow = float(pi) * (float(promien_kola) ** 2)

print("Pole powierzchni koła o zadanym promieniu  r = " + str(promien_kola) + " wynosi = " + str(round(pole_pow, 3)))