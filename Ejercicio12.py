barra = 3.49
descuento = round(barra * 0.6, 2)
barranodia = barra - descuento
nbarras= int(input("Introduce el número de barras vendidas que no son del día: "))
total = round(barranodia * nbarras, 2)
print("El precio de una barra de pan fresca es de " + str(barra) + ", al no ser frescas se hace un descuento de " + str(descuento) + ", el coste final total es de " + str(total))
