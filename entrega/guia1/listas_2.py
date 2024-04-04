#creaccion de listas usando el metodo
#nombres=list[]
#crear una lista con valores iniciales
nombres=list(['Gaston', 'eva', 'lautaro'])
#print(nombre)
#metodos, aappend, permiete agregar un elemento al final de la lista
nombres.append('sandra')
#utilizar funcion id, nos da una referencia dentro de nuestro programa 
print(id(nombres))
#insert
nombres.insert(0,'victoria')
#print(nombre)

#utiliizar el operador in
#for nombre in nombres:
#    print(nombre)

#mutabilidad cambiar elemento
nombres[4]='Lorenzo'
for nombre in nombres:
    print(nombre)

#lista tammbien para mostrar datos

#rebanadas y listas
