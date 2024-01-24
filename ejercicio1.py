import os
os.system('cls')

print("Bienvenido usuario")

voltaje1=int(input("ingrese voltaje 1: "))
voltaje2=int(input("ingrese voltaje 2: "))
voltaje3=int(input("ingrese voltaje 3: "))
voltaje4=int(input("ingrese voltaje 4: "))
voltaje5=int(input("ingrese voltaje 5: "))

promedio=(voltaje1+voltaje2+voltaje3+voltaje4+voltaje5/ 5)
print(f"el promedio de los 5 voltajes es: {promedio}")

if(promedio>220):
    print("alto voltaje")

elif(promedio<220):
    print("voltaje correcto")

else:
    print("error")

