print("Hej!")
print("Witaj w programie przeliczania wartości temperatury w stopniach Celsjusza na Fahrenhejta.")
temp_celsjusz = input("Podaj wartość temperatury w stopniach Celsjusza: ")
print("")

print("Wzór na konwersję: ℉ = (℃ * 1.8) + 32.0")

temp_fahrenhejt = (float(temp_celsjusz) * 1.8) + 32.0
print("")
print("Wartość temperatury w stopniach Celsjusza: " + str(temp_celsjusz) +" ℃" )
print("Wartość temperatury w stopniach Fahrenhejta: " + str(round(temp_fahrenhejt, 2)) + " ℉" )

