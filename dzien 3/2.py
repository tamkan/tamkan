liczba = 15

if(liczba % 3 == 0 and liczba % 5 == 0):
    print("Liczba podzielna przez 3 i 5")
elif(liczba % 3 == 0 or liczba % 5 == 0):
    print("Liczba podzielna przez 3 lub 5")
elif (liczba % 3 == 0):
    print("Liczba podzielna przez 3")
elif(liczba % 5 == 0):
    print("Liczba podzielna przez 5")
else:
    print("nie podzielna przez 3 i 5")

###
range1 = range(1,40000000)
lista1 = [1, 2, 3, "napis"]
lista2 = list("dwa")
lista3 = list(lista1)
print(range1)
print((type(lista1)))
print(lista2)
print(lista3)

lista4 = ["raz", "dwa", "trzy"]
del(lista4[0])

print(lista4.pop())
print(lista4)


###

lista = [[2,3,4],[4,5,6],[7,8,9]]
lista = [
    [2,3,4],
    [4,5,6],
    [7,8,9]
]

print(lista[1][2])

lista = [
    [2,3,4],
    [4,5,6, "NAPIS"],
    [7,8,9]
]

print(lista[1][3][3])

###

krotka1 = (1, 2, 3)
krotka2 = ("kwiatek", "doniczka", "ziemia", "domek")
krotka3 =()
krotka4 = (1, "dwa", 3)
krotka5 = (tuple)

###

