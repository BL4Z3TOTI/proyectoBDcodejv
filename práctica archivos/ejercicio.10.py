def eliminar_lineas_vacias(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
            for linea in entrada:
                if linea.strip():  # Verifica si la línea no está vacía después de quitar espacios
                    salida.write(linea)
        print(f"Las líneas vacías de '{archivo_entrada}' han sido eliminadas y guardadas en '{archivo_salida}'.")
    except FileNotFoundError:
        print(f"El archivo '{archivo_entrada}' no fue encontrado.")

# Ejemplo de como se usaria:
eliminar_lineas_vacias("con_vacias.txt", "sin_vacias.txt")