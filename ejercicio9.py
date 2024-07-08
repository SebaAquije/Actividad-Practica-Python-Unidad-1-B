# 9) Cree un programa que calcule el promedio de un alumno, ingresando su nombre apellido, 3 notas, que muestre al final las leyendas pertinentes.

nombreAlumno = input("Nombre: ")
apellidoAlumno = input("Apellido: ")
notaA = float(input("Primer nota: "))
notaB = float(input("Segunda nota: "))
notaC = float(input("Tercer nota: "))

promedio = (notaA + notaB + notaC)/ 3
print("El promedio final de " + nombreAlumno + " " + apellidoAlumno + " es " + str(promedio))
