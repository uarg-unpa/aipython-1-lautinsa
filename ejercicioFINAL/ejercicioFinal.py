import random

def lanzar_dado(cantidad, caras):
    return [random.randint(1, caras) for _ in range(cantidad)]

def calcular_resultados(resultados):
    total = sum(resultados)
    return total

def mostrar_estadisticas(resultados):
    cantidad = len(resultados)
    minimo = min(resultados)
    maximo = max(resultados)
    promedio = sum(resultados) / cantidad

    print(f"--- Estadísticas de los lanzamientos ---")
    print(f"Cantidad de lanzamientos: {cantidad}")
    print(f"Valor mínimo obtenido: {minimo}")
    print(f"Valor máximo obtenido: {maximo}")
    print(f"Promedio de los resultados: {promedio:.2f}")

def main():
    print("Bienvenido al simulador de lanzamiento de dados!")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de dados a lanzar: "))
            caras = int(input("Ingrese el número de caras de cada dado: "))
            lanzamientos = int(input("Ingrese la cantidad de lanzamientos: "))
            
            resultados_totales = []
            for _ in range(lanzamientos):
                resultados = lanzar_dado(cantidad, caras)
                resultados_totales.extend(resultados)
                print(f"Resultados del lanzamiento: {resultados}")
                print(f"Suma de resultados: {calcular_resultados(resultados)}")

            print("\nResultados totales:")
            print(f"Resultados totales: {resultados_totales}")
            print(f"Suma total: {calcular_resultados(resultados_totales)}")

            mostrar_estadisticas(resultados_totales)

        except ValueError:
            print("Por favor, ingrese un número válido.")

        continuar = input("¿Desea lanzar más dados? (s/n): ")
        if continuar.lower() != 's':
            break

    print("Gracias por usar el simulador de lanzamiento de dados!")

if __name__ == "__main__":
    main()
