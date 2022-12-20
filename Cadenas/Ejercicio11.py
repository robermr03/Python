nombre = input("Introduzca el nombre del producto: ")
precio = float(input("Introduzca el precio del producto: "))
unidades = int(input("Introduzca el número de unidades del producto: "))

print('{nombre}: {unidades} unidades x {precio}€ = {total}€'.format(nombre = nombre, unidades = unidades, precio = precio, total = unidades * precio))