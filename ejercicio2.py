import os
os.system('cls')

basetriangulo = 0
alturatriangulo = 0
area = (basetriangulo * alturatriangulo) / 2

basetriangulo = float(input("Ingrese la base: "))
alturatriangulo = float(input("Ingrese la altura: "))
area = (basetriangulo * alturatriangulo) / 2

if area > 1000:
  print("Datos no validos")
else:
  print("El area del triangulo es: ",area)