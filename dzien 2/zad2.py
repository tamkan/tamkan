print("Hej!")
print("Witaj w programie przeliczania wartości temperatury w stopniach Fahrenhejta na Celsjusza.")
temp_fahrenhejt = input("Podaj wartość temperatury w stopniach Fahrenhejta: ")
print("")

print("Wzór na konwersję: ℃ = (℉ - 32) / 1.8")

temp_celsjusz = (float(temp_fahrenhejt) - 32) / 1.8

print("")
print("Wartość temperatury w stopniach Fahrenhejta: " + str(temp_fahrenhejt) + " ℉" )
print("Wartość temperatury w stopniach Celsjusza: " + str(round(temp_celsjusz, 2)) + " ℃" )