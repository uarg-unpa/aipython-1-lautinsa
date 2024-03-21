#mostrar los numeros desde el 0 hasta el 10 
contador=0
while contador <=10:
    print(contador, end='-')
    contador=contador+1
print()
print("Fin de la iteracion")

#for (coleccion):
cadena="AIPYTHON"
for letra in cadena:
    print (letra , end='-')

#range ()
for num in range(10):
    print (num) 
#te lee la cadena que da 8 y despues junto con la cadena y len va range y te da 7.   
for indice in range(len(cadena)):
    print(cadena[indice])
#salta en dos.    
for num in range (0,10,2):
    print(num)

#imprimir 10 veces AIPYTHON
for _ in range(10):
    print ("AIPYTHON")