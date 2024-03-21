#strip eliminar espacios en blancos los principios y al final.
#inmutables 
#cadena= "AIPYHTON"
#print (cadena[5])
#cadena[5]='h'
#error ya que no se puede cambiar los literarios
#programa

frase=input("Ingrese una frase")
caracter=input("Ingrese caracter")
#buscar la primera aparicion del caracter
posicion=frase.find(caracter)

if posicion != -1:
    print(f"El caracter {caracter} se encuentra en la posicion {posicion+1}")
    subcadena=frase[posicion:]
    print(f"Subcadena a partir de la posicion {posicion+1}: {subcadena}")
else: 
    print(f"El caracter {caracter} no se encuentra en la frase")


#como no hacer bucles infinitos, 1 inicializacion de la variable ,2 evaluar la condicion con la variable 1, 3 actualizacion dentro del bucle 
#