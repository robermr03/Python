email = input("Introduzca su email: ")
dominio = "ceu.es"
dominio1 = email.split("@")[1]
print(email.replace(dominio1, dominio))