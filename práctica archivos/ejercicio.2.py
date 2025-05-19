import os

def eliminar_txt(carpeta):
    for nombre_archivo in os.listdir(carpeta):
        if nombre_archivo.endswith(".txt"):
            ruta_completa = os.path.join(carpeta, nombre_archivo)
            confirmacion = input(f"¿Desea eliminar '{nombre_archivo}'? (s/n): ")
            if confirmacion.lower() == 's':
                os.remove(ruta_completa)
                print(f"Archivo '{nombre_archivo}' eliminado.")
            else:
                print(f"Archivo '{nombre_archivo}' no eliminado.")

# Ejemplo de como se usaria:
eliminar_txt("mi_carpeta")
