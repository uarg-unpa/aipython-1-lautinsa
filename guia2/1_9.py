#1  hacer un if y dentro de ese if, en else usar una variable para saber la diferencia de edad que falta.
# edad=int(input("Ingrese su edad: "))
# if edad >=18:
#     print("Tiene la edad suficiente para conducir")
# else:
#     años_faltantes=18-edad
#     print(f"Te faltan {años_faltantes}")

#2
# edadProfe=40
# edad_user= int(input("Ingrese su edad: "))
# if edad_user >40:
#     print("Sos mayor que el profesor")
# elif edad_user ==40:
#     print("¡Por casualiades de la vida tienes la misma edad que el profesor!")
# else:
#     diferencia=40-edad_user
#     print(f"Sos menor que el profesor, te faltan {diferencia} años para alcanzar al profesor.")

#3 contraseña
# contraAlmacenada="riverplate"
# password=str(input("Ingrese su contraseña: "))
# if password==contraAlmacenada:
#     print("Contraseña correcta")
# else:
#     print("Contraseña incorrecta")

#4 
# a=int(input("Ingrese número A: "))
# b=int(input("Ingrese número B: "))
# if a > b:
#     print("A es mayor que B")
# elif a < b:
#     print("A es menor que B")
# else:
#     igual=a==b
#     print("Los números son iguales")

#5
num=int(input("Ingrese un número"))
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")