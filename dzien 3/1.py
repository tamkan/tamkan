zmienna = r"to jest jakis \ntekst"
print(zmienna)

zmienna = 'to jest jakis: "tekst"'
print(zmienna)

zmienna = "to jest jakis: 'tekst'"
print(zmienna)

napis = 23

zmienna = f"to jest napis: (napis)"
print(zmienna)

zmienna = "to jest napis: " + str(napis)
print(zmienna)

zmienna = 12.33
print("zmienna %s" % zmienna)
print("zmienna %f" % zmienna)
print("zmienna %d" % zmienna)

print("To jest {} sposób na wprowadzenie {}".format(3, 'zmiennych'))
print("To jest {ilosc} sposób na wprowadzenie {nazwa}".format(nazwa='zmiennych', ilosc=3))


# +-----+
# /     /
# /     /
# /     /
# +-----+

szerokosc = 10
wysokosc = 20

print('+' + ("-" * szerokosc) + '+')
print(('|' + (" " * szerokosc) + '|\n')*wysokosc, end='')
print('+' + ("-" * szerokosc) + '+')


top_bottom = '+' + ("-" * szerokosc) + "+"
print(top_bottom + ('|' + (" " * szerokosc) + '|\n')*wysokosc + top_bottom, end="")

###

import string
print(string.ascii_letters)

print("(:.1f")
