def suma_lineas(nombre_archivo):
    sumas_por_linea = []
    with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                numeros_str = linea.strip().split()
                suma_linea = sum(int(numero) for numero in numeros_str)
                sumas_por_linea.append(suma_linea)
    return sumas_por_linea
resultado_lineas = suma_lineas('datos1.txt')
print(resultado_lineas)
def suma_columnas(nombre_archivo):
    columnas = [[], [], []]
    with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                numeros_str = linea.strip().split()
                columnas[0].append(int(numeros_str[0]))
                columnas[1].append(int(numeros_str[1]))
                columnas[2].append(int(numeros_str[2]))
    sumas_columnas = [sum(col) for col in columnas]
    return sumas_columnas
resultado_columnas = suma_columnas('datos1.txt')
print(resultado_columnas)