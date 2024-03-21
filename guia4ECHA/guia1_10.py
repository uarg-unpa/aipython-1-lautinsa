#1
# def multiplicacion(num1, num2):
#     return num1 * num2
# numero1 = int(input("Ingrese el numero 1: "))
# numero2 = int(input("Ingrese el numero 2: "))
# resultado = multiplicacion(numero1, numero2)
# print("El resultado de la multiplicación entre", numero1, "y", numero2, "es:", resultado)

#2
# def multiplicacion(num1=1, num2=1):
#     return num1 * num2
# resultado1 = multiplicacion()
# resultado2 = multiplicacion(5, 7)
# print("El resultado de la multiplicación sin argumentos es:", resultado1)
# print("El resultado de la multiplicación entre 5 y 7 es:", resultado2)

#3
# def mensaje_creativo(nombre):
#     return f"¡Hola {nombre}! Bienvenido al mundo de la creatividad."
# nombre_usuario = input("Por favor, introduce tu nombre: ")
# mensaje = mensaje_creativo(nombre_usuario)
# print(mensaje)

#4
# def tabla_multiplicar(numero):
#     print(f"Tabla de multiplicar del {numero}:")
#     for i in range(1, 11):
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado}")
#         print("." * len(f"{numero} x {i} = {resultado}"))

# numero = int(input("Ingrese un número: "))
# tabla_multiplicar(numero)

#5
# def es_par_o_impar(numero):    
#     if numero % 2 == 0:
#         return "par"
#     else:
#         return "impar"
# numero = int(input("Ingrese un número: "))
# resultado = es_par_o_impar(numero)
# print(f"El número {numero} es {resultado}.")

#6
# def factorial(numero):
#     resultado = 1
#     for i in range(1, numero + 1):
#         resultado *= i
#     return resultado
# numero = int(input("Ingrese un número: "))
# resultado = factorial(numero)
# print(f"El factorial de {numero} es {resultado}.")

#7
# def maximo_de_tres(num1, num2, num3):
#     return max(num1, num2, num3)
# numero1 = float(input("Ingrese el primer número: "))
# numero2 = float(input("Ingrese el segundo número: "))
# numero3 = float(input("Ingrese el tercer número: "))

# maximo = maximo_de_tres(numero1, numero2, numero3)
# print("El máximo de los tres números es:", maximo)

#8
# def invertir_string(cadena):
#     return cadena[::-1]
# cadena_original = input("Ingrese una palabra: ")
# cadena_invertida = invertir_string(cadena_original)
# print("La cadena invertida es:", cadena_invertida)

#9
# def es_palindromo(cadena):
#     cadena = cadena.lower().replace(" ", "")

#     return cadena == cadena[::-1]

# cadena = input("Ingrese una cadena: ")
# if es_palindromo(cadena):
#     print("La cadena es un palíndromo.")
# else:
#     print("La cadena no es un palíndromo.")

#10
# def fahrenheit_a_celsius(fahrenheit):
#     celsius = (5 / 9) * (fahrenheit - 32)
#     return celsius
# temperatura_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
# temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
# print(f"{temperatura_fahrenheit} grados Fahrenheit son equivalentes a {temperatura_celsius:.2f} grados Celsius.")
