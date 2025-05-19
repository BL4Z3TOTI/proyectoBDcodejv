import os

def renombrar_archivos(carpeta):
    archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
    for i, nombre_archivo in enumerate(archivos):
        nuevo_nombre = f"{i+1}_{nombre_archivo}"
        ruta_antigua = os.path.join(carpeta, nombre_archivo)
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)
        os.rename(ruta_antigua, ruta_nueva)
        print(f"Renombrado '{nombre_archivo}' a '{nuevo_nombre}'.")

# Ejemplo de como se usaria:
renombrar_archivos("mi_carpeta")    

   