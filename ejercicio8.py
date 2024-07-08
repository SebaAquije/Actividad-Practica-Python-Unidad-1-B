# 8) Cree un programa que permite ingresar el nombre de un producto, el precio y que calcule el IVA.

nombreProd = ("Ingrese el nombere del producto: ")
precioProd = float(input("Ingrese el precio del producto: "))
precioFinal = float((precioProd * .21) + precioProd)

print("El valor final del producto con IVA incluido es: " + str(precioFinal) + ".")
