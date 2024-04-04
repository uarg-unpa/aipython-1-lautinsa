#1 iterar 0 a 100
#numero=0
# while numero <= 100:
#     print(numero)
#     numero += 1 #si no hago esto, es infinito.

#2 for tip range, uno al lado del otro.
#numero=0
# for numero in range(101):
#     print(numero, end=' ')

#3
# numero=10
# while numero >= 0:
#     print(numero)
#     numero-=1 #se usa para saber como es el secuensiado.

#4
# inicio = int(input("Ingrese el primer número entero: "))
# fin = int(input("Ingrese el segundo número entero: "))

# print("Números entre", inicio, "y", fin,":")

# if inicio < fin:
#     for numero in range(inicio, fin + 1):
#         print(numero, end=" ")
# else:
#     for numero in range(inicio, fin - 1, -1):
#         print(numero, end=" ")

#5
# for i in range(1, 8):  
#     print("#" * i)   

#6
# for i in range(7): 
#     fila = ""       
#     for j in range(8):  
#         fila += "#"    
#     print(fila)     

#7
# nombre_usuario = input("Ingrese su nombre de usuario: ")
# numero = int(input("Ingrese un número entero: "))

# for i in range(numero):
#     print(nombre_usuario)

#8
# numero = int(input("Ingrese un número entero positivo mayor a 3: "))
# if numero <= 3:
#     print("El número ingresado no es válido. Debe ser mayor a 3.")
# else:
#     print("Números impares desde 1 hasta", numero, ":")
#     for i in range(1, numero + 1, 2):
#         print(i)

#9
# for i in range(11):
#     resultado = i * i  
#     print(f"{i} x {i} = {resultado}")

#10
# numero = int(input("Ingrese un número entero: "))
# for i in range(1, numero + 1, 2):
#     impares = list(range(i, 0, -2))
#     fila = ' '.join(map(str, impares))
#     print(fila)    

#11
# N = int(input("Ingrese un número natural: "))
# suma = 0
# for i in range(1, N + 1):
#      suma += i
# print(i, end="")
# if i < N:
#         print(" + ", end="")
# print(" =", suma)

#12
# N = int(input("Ingrese un número natural: "))
# suma = 0
# for i in range(2, 2*N + 1, 2):
#     suma += i
# print("La suma de los primeros", N, "números pares es:", suma)

#13
# numero1 = int(input("Ingrese el primer número entero: "))
# numero2 = int(input("Ingrese el segundo número entero: "))
# menor = min(numero1, numero2)
# mayor = max(numero1, numero2)
# print("Números pares entre", menor, "y", mayor, ":")
# for numero in range(menor, mayor + 1):
#     if numero % 2 == 0:
#         print(numero)
