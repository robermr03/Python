capital = input("Introduce el capital inicial: ")
primer = round(float(capital) + float(capital)*0.04, 2)
segundo = round(float(primer) + float(primer)*0.04, 2)
tercer = round(float(segundo) + float(segundo)*0.04, 2)

print("Los ahorros tras el primer año son " + str(primer) + ", tras el segundo año " + str(segundo) + ", tras el tercer año " + str(tercer))