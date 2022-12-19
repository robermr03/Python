capital = float(input("Introduce el capital de la inversión: "))
interes = 0.04
primer = round(float(capital + capital*interes), 2)
segundo = round(float(primer + primer*interes), 2)
tercer = round(float(segundo + segundo*interes), 2)

print("Después del primer año los ahorros son de: " + str(primer))
print("Después del segundo año los ahorros son de: " + str(segundo))
print("Después del tercer año los ahorros son de: " + str(tercer))