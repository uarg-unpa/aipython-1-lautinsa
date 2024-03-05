#sentencia if
edad= int(input("ingrese su edad: "))
if edad >=18:
    print("Ud debe votar")
else: print("Usted es menor de 18 años")
print("Fuera del bloque if")

calificacion= int(input("Ingrese calificación: "))
if calificacion >=90:
    print("Excelente")
elif calificacion >=80:
    print("Muy Bien")
elif calificacion>=70 :
    print("Bien")
else:
    print("Insuficiente")