cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el intereés anual: "))
años = float(input("Introduce los años de la inversión: "))
capital = str(round(cantidad * (interes / 100 + 1) ** años, 2))

print("El capital obtenido por la inversión es " + capital + "€")