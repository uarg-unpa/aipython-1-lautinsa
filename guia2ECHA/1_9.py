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
# num=int(input("Ingrese un número: "))
# if num c:
#     print("El numero es par")
# else:
#     print("El numero es impar")

#6
# numeroSemana=int(input("Ingrese un número del 1 al 7: "))
# if numeroSemana == 1:
#     print("Hoy es Lunes")
# elif numeroSemana ==2:
#     print("Hoy es Martes")
# elif numeroSemana ==3:
#     print("Hoy es Miercoles")
# elif numeroSemana ==4:
#     print("Hoy es Jueves")
# elif numeroSemana ==5:
#     print("Hoy es Viernes")
# elif numeroSemana ==6:
#     print("Hoy es Sabado")
# elif numeroSemana ==7:
#     print("Hoy es Domingo")
# else:
#     numeroSemana > 7
#     print("No existe otro dia")
 
#7 utilizacion de and para capar la variable 
# calificacion=int(input("Ingrese calificación: "))
# if calificacion >=100 and calificacion >= 80:
#     print("A")
# elif calificacion >=70 and calificacion < 79:
#     print("B")
# elif calificacion >=60 and calificacion < 69:
#     print("C")
# elif calificacion >=50 and calificacion < 59:
#     print("D")
# elif calificacion >=0 and calificacion < 49:
#     print("F")

#8 edad? mostrar el precio de la entrada, cliete < 4 = gratis, cliente >=4 and cliente <=18, paga 5 , cliente > 18, paga 10

# edadCliente=int(input("Ingrese su edad: "))
# if edadCliente < 4:
#     print("Pase gratis!")
# elif edadCliente >=4 and edadCliente <=18:
#     print("Paga 5")
# else:
#     edadCliente > 18
#     print("Paga 10")

#9 impuesto=x, 18 > para pagar el impuesto, y tambien tiene que tener $100000 > ingresos   

# ingresosMensuales=int(input("Ingresos mensuales: "))
# edadUsuario=int(input("Ingrese su edad: "))

# if edadUsuario > 18 and ingresosMensuales >= 100000:
#     print("Tienes que pagar impuestos")
# else:
#     print("No debes pagar impuestos")