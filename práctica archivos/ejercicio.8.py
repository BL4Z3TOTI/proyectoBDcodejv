def contar_info_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            lineas = contenido.splitlines()
            num_lineas = len(lineas)
            palabras = contenido.split()
            num_palabras = len(palabras)
            num_caracteres = len(contenido)
            print(f"Archivo: {nombre_archivo}")
            print(f"Líneas: {num_lineas}")
            print(f"Palabras: {num_palabras}")
            print(f"Caracteres: {num_caracteres}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")

# Ejemplo de como se usaria:
contar_info_archivo("texto.txt")

