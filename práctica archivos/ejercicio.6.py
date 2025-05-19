def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea.rstrip('\n'))  
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")

# Ejemplo de como se usaria:
leer_archivo("texto.txt")
with open("texto.txt", 'w') as f:
    f.write("Esta es una línea.\nEsta es otra líkfnkdndnlmdbndbnea.\nY esta es la última línea.\n")
leer_archivo("texto.txt")
import os