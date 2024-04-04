#listasnson indexada, pueden almaccenar literale, almacenar objetos, se pueden unir, son iterables podemos recorres los elementos. Es mutable (modificable)
#creacion lista vacia 
nombres=[]
#valores iniciales 
nombres=['Franco', 'Fernanda', 'Alejandro', 'Fabiana']
#mostrar lista
print(nombres)
#iterar  sobre lista len se puede aplicar a otraaas colecciones 
for  i in range(len(nombres)):
    print(nombres[i])
#acccedemos a los elementos
#accedemos al prrimer elemento
primer__eelemento=nombres[0]
print(f"El primer elemento es {primer__eelemento}")

#repaso de funciones
# prin() len() input() son independientes y asii son invocacciones

#metodos son funciones pero perteneccen aa alguien
#cadena="AIPYTHON"
#cadena.upper()