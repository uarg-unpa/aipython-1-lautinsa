#1
#lista_vacia = []

#2
#lista_mas_7_elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#3
#print(len(lista_mas_7_elementos))

#4
# frutas_favoritas = ['manzana', 'banana', 'naranja', 'uva']
# print(len(frutas_favoritas))
# del frutas_favoritas[0]
# frutas_favoritas.append('pera')
# print(len(frutas_favoritas))
# print(frutas_favoritas)

#5
# lista_dada = [1, 2, 3, 4, 5]
# primer_elemento = lista_dada[0]
# elemento_del_medio = lista_dada[len(lista_dada) // 2]
# ultimo_elemento = lista_dada[-1]
# print(primer_elemento, elemento_del_medio, ultimo_elemento)

#6
# datos_personales = ['Lautaro', 19, 1.70, 'Soltero', 'Don Bosco']

#7
# companias_favoritas = ['Google', 'Apple', 'Amazon']
# for compania in companias_favoritas:
#     print(compania)
# for indice, compania in enumerate(companias_favoritas):
#     print(f"{indice}: {compania}")
# companias_favoritas[0] = 'Microsoft'
# print(companias_favoritas)

#8
# numeros_del_1_al_10 = list(range(1, 11))
# print(numeros_del_1_al_10[:3])

#9
# letras_de_a_a_j = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# print(letras_de_a_a_j[1::2])

#10
# lista_propia = [10, 'hola', True, 3.14, [1, 2, 3]]
# print(lista_propia[::-1])

#11
# palabras_favoritas = ['python', 'programación', 'computadora', 'videojuegos', 'futbol']
# sub_lista_palabras = palabras_favoritas[1:4]
# print(sub_lista_palabras)

#12
# flores = ['rosas', 'orquídea', 'lirio', 'tulipan', 'margarita', 'dalia', 'hortensia']
# print(flores[2:5])
# print(flores[1::2])
# print(flores[::3])

#13
# def contar_vocales(lista_caracteres):
#     vocales = 'aeiouAEIOU'
#     cantidad_vocales = sum(1 for caracter in lista_caracteres if caracter in vocales)
#     return cantidad_vocales
# lista_caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print("La cantidad de vocales en la lista es:", contar_vocales(lista_caracteres))

#14
# def intercalar_listas(lista1, lista2):
#     intercalada = []
#     for elemento1, elemento2 in zip(lista1, lista2):
#         intercalada.append(elemento1)


#15
# def calcular_promedio(lista_numeros):
#     if not lista_numeros:
#         return 0
#     suma_numeros = sum(lista_numeros)
#     cantidad_numeros = len(lista_numeros)
#     promedio = suma_numeros / cantidad_numeros
#     return promedio
# lista_numeros = [1, 2, 3, 4, 5]
# promedio = calcular_promedio(lista_numeros)
# print("El promedio de los números en la lista es:", promedio)
        