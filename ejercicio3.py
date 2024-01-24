import os
os.system('cls')

print("Bienvenido")
voltaje=int(input("ingrese voltaje 1: "))

voltaje=int(input("ingrese voltaje 2: "))

voltaje=int(input("ingrese voltaje 3: "))
promedio=("voltaje1+voltaje2+voltaje3/ 3")

if(promedio<115):
    print("voltaje correcto")

elif(promedio>115 and promedio<220):
    print("alto voltaje")

else:
    if(promedio>220):
     print("PELIGRO")