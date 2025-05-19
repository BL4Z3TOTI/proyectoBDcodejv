import os

def contar_archivos(Escritorio):
    contador = 0
    for elemento in os.listdir(Escritorio):
        ruta_completa = os.path.join(Escritorio, elemento)
        if os.path.isfile(ruta_completa):
            contador += 1
    return contador

# Ejemplo de como se usaria:
num_archivos = contar_archivos("mi_carpeta")
print(f"Hay {num_archivos} archivos en la carpeta.")

