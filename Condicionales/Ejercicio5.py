edad = int(input("Introduzca su edad: "))
ingresos = float(input("Introduzca sus ingresos mensuales: "))
if edad > 16 and ingresos >= 1000:
    print("Tiene que tributar")
else:
    print("No tiene que tributar")