#15 
# sociedad='aiPython P1'
# print(f"{sociedad}")
# leN=len(sociedad)
# print(f"Usando len: {leN}")
# print(sociedad.upper())
# print(sociedad.lower())

#16
# texto= ("sometimes it is the people no one imagines anything of who do the things that no one can imagine.")
# capitalize=texto.capitalize()
# title=texto.title()
# swapcase=texto.swapcase()
# print(capitalize)
# print(title)
# print(swapcase)

#17 tres veces
# nombre=str(input("Ingrese su nombre completo: "))

# tresVeces=nombre*3

# print(tresVeces)

#18 arbol
# print("           *       ")
# print("         ** **     ")
# print("       ***   ***   ")
# print("        *     *    ")
# print("      ****   ****  ")
# print("        *     *    ")
# print("        *     *    ")
# print("        *******    ")

#19
#print("    *\n   / \\\n  /   \\\n /     \\\n/       \\\n ")

#20 error 
# arbol1 = "    *\n   / \\\n  /   \\\n /     \\\n/       \\\n"
# arbol2 = "      *\n     / \\\n    /   \\\n   /     \\\n  /       \\\n"

# print(arbol1 + arbol2)

#21 �
# palabra=str(input("Ingrese una palabra: "))
# remplazo=palabra.replace("a", "�")
# print(remplazo)

#22
# frase = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"
# espacios_cortados = 0
# for i in range(len(frase)):
#     if frase[i] == ' ':
#         espacios_cortados += 1
#         if espacios_cortados == 3:
#             frase_cortada = frase[i+1:]
#             break

# print(frase_cortada)

#23 remover espacios en blanco // strip
# frase="     La ciencia es una ecuación diferencial. La religión es una condición de frontera. "
# fraseSinEspacio= frase.strip()

# print(fraseSinEspacio)

#24 \n salto en linea 
# textoSep="El razonamiento matemático puede considerarse más bien esquemáticamente como \n el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio"
# print(textoSep)

#25 salto \n, tabulacion \t
# print("Nombre\tEdad\tPais\tCiudad")
# print("Alexa\t250\tUSA\tCapeCod")
