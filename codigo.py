import os

def recuperar_nombres(ruta_carpeta_principal):

    nombres_subcarpetas = []
    for nombre in os.listdir(ruta_carpeta_principal):
        ruta_completa = os.path.join(ruta_carpeta_principal, nombre)
        if os.path.isdir(ruta_completa):
                nombres_subcarpetas.append(nombre)
    return nombres_subcarpetas
nombres_actores = recuperar_nombres('train')
print(f"Nombres de las carpetas encontradas: {nombres_actores}")

def obtener_nombres_imagenes(ruta_carpeta_principal):
    nombres_imagenes_por_clase = []
    for root, dirs, files in os.walk(ruta_carpeta_principal):
        if files:
            nombres_imagenes_por_clase.append(files)
    return nombres_imagenes_por_clase
nombres_imagenes = obtener_nombres_imagenes('train')
print(f"Nombres de las imágenes encontradas: {nombres_imagenes}")