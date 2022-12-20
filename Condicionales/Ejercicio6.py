nombre = input("Introduzca su nombre: ")
sexo = input("Introduzca su sexo (M / H): ")
grupo = "A";
if sexo == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Perteneces al grupo {}".format(grupo))
