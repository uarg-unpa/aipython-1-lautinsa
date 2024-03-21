# num=2
# def multiplicacion(x):
#     num=3
#     return x*num
# print(multiplicacion(4))

#la varieble es alcanzable, sombreado sombreaar la variable afuera y utilizar la que esta adentro

# def mensaje ():
#     alternativo="mas sobre programacion"

#devolver y asignar mejor estrategia para seguir!!!

def  mutables(lista):
    lista[2]=35

mis_numeros= [1,2,3]
print(f"Antes de invocar a la funcion")
print(mis_numeros)
mutables(mis_numeros)
print("Despues dde llamar a la funcion mutable")
print(mis_numeros)
    