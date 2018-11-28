#program rysujący piramidkę

wysokosc = int(input("Podaj wysokosc piramidy:  "))

for i in range(1, wysokosc,2):
    print(" "*(wysokosc - i) + "#"*i)
