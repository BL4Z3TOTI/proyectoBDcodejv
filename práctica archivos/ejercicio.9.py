def invertir_archivo(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
            for linea in entrada:
                salida.write(linea.rstrip('\n')[::-1] + '\n')
        print(f"El contenido de '{archivo_entrada}' ha sido invertido y guardado en '{archivo_salida}'.")
    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no fue encontrado.")

# Ejemplo de como se usaria:
invertir_archivo("texto.txt", "invertido.txt")