#break finaliza el bucle
#continue pasa a la siguiente iteracion
suma=0
for i in range (1,30): 
    print (i)
    if i > 10:
        continue
    suma=suma+i
print(suma)

num=int(input())
while num >9:
    if num%2==2