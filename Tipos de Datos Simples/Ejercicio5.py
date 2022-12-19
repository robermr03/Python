horas = int(input("Introduce el número de horas trabajadas: "))
coste = float(input("Introduce el coste por hora: "))
total = round(horas * coste, 2)

print("El coste total por las horas trabajadas es de " + str(total))