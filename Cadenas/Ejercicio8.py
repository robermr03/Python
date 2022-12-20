precio = input("Introduzca el precio de un producto en euros con dos decimales: ")
print(precio[:precio.find('.')] + " euros y " + precio[precio.find('.') + 1:] + " céntimos")
